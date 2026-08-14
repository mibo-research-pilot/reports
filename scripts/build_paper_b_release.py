#!/usr/bin/env python3
"""Build and validate the deterministic MIBO Paper B evidence release."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
RELEASE_ID = "mibo-paper-b-pilot-evidence-v1.0.0"
BUNDLE_NAME = "MIBO_Paper_B_Pilot_Evidence_v1.0.0"
ZIP_NAME = f"{BUNDLE_NAME}.zip"
CORE_SHA = "5f8dc0a21dcc73930f6ebc27cbd67dada3105a0e"
QUERIES_SHA = "49144025fee43b6599892ad0a270c09c518ff815"
REPORTS_EVIDENCE_SHA = "005b98c55158e95c71b1f4d963c04d4dcf2fd5f0"
INSTRUMENT_SHA = "8463f51cf40bd0e2b7186569cdb84e26085ad16f6c62e7035c1a1c59311cdd35"
FIXED_ZIP_TIME = (2026, 7, 28, 0, 0, 0)
MANIFEST_SOURCE = ROOT / "paper-b" / "release" / "MANIFEST.json"
OUTER_HASH_SOURCE = ROOT / "paper-b" / "release" / "SHA256SUMS.json"

EXPECTED_QUERY_TEXTS = {
    "q001": "おすすめのプロジェクト管理ツールは？",
    "q002": "What is the best CRM for small businesses?",
    "q003": "睡眠の質を上げる方法を教えて",
    "q004": "How do I implement RAG with a vector database?",
    "q005": "日本の代表的なAI研究者を5人挙げて",
}

RELEASE_METADATA = (
    ("paper-b/release/README.md", "README.md", "release_metadata", "Explains release scope, integrity checks, provenance, corrections, and citation status."),
    ("paper-b/RELEASE_LOCK.json", "RELEASE_LOCK.json", "release_metadata", "Locks the immutable evidence boundary and source repository commits."),
    ("paper-b/release/RELEASE_NOTES.md", "RELEASE_NOTES.md", "release_metadata", "Drafts the release purpose, boundaries, integrity policy, and limitations."),
    ("paper-b/release/SOURCE_REPOSITORIES.json", "SOURCE_REPOSITORIES.json", "provenance", "Records repository roles, pinned commits, extraction methods, and validation state."),
    ("paper-b/release/RIGHTS_AND_LICENSES.md", "RIGHTS_AND_LICENSES.md", "license_or_rights", "Separates source-specific licenses and unresolved provider or third-party rights."),
    ("paper-b/release/ZENODO_METADATA_DRAFT.md", "ZENODO_METADATA_DRAFT.md", "release_metadata", "Provides human-reviewable deposit metadata without claiming a DOI or publication."),
)


@dataclass(frozen=True)
class BundleFile:
    bundle_path: str
    data: bytes
    source_repository: str
    source_commit: str | None
    source_path: str
    role: str
    inclusion_rationale: str
    source_state: str = "pinned_git_blob"

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def load_json_bytes(data: bytes, label: str) -> Any:
    try:
        return json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid UTF-8 JSON: {label}: {error}") from error


def git(repo: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(f"git {' '.join(args)} failed in source repository: {detail}")
    return result.stdout


def verify_commit(repo: Path, expected_sha: str, repository_name: str) -> None:
    require(repo.is_dir(), f"source repository path is missing: {repository_name}")
    git(repo, "cat-file", "-e", f"{expected_sha}^{{commit}}")
    resolved = git(repo, "rev-parse", f"{expected_sha}^{{commit}}").decode("ascii").strip()
    require(resolved == expected_sha, f"pinned commit mismatch: {repository_name}")


def tracked_paths(repo: Path, commit: str) -> list[str]:
    raw = git(repo, "ls-tree", "-r", "-z", "--name-only", commit)
    paths = [item.decode("utf-8") for item in raw.split(b"\0") if item]
    require(paths == sorted(paths), "Git tree paths are not sorted")
    require(len(paths) == len(set(paths)), "Git tree contains duplicate paths")
    require(all(".git" not in PurePosixPath(path).parts for path in paths), "Git metadata path found in tracked snapshot")
    return paths


def git_blob(repo: Path, commit: str, path: str) -> bytes:
    return git(repo, "show", f"{commit}:{path}")


def classify_core(path: str) -> str:
    if path == "LICENSE":
        return "license_or_rights"
    if path == "AUDIT.md":
        return "provenance"
    if path.startswith(".github/") or path.startswith("scripts/") or path == ".gitignore":
        return "validation"
    if path == "paper-b/README.md" or path == "CITATION.cff":
        return "release_metadata"
    return "conceptual_context"


def classify_query(path: str) -> str:
    if path == "LICENSE":
        return "license_or_rights"
    if path == "HASHES.json":
        return "integrity_manifest"
    if path.startswith("v0.1") and path.endswith(".json"):
        return "query_instrument"
    if path.startswith(".github/") or path.startswith("scripts/"):
        return "validation"
    return "provenance"


def classify_report(path: str) -> str:
    if path == "LICENSE":
        return "license_or_rights"
    if path.endswith("-observation.md"):
        return "observation_report"
    if path.endswith("/run_metadata.json"):
        return "provenance"
    if path.endswith("/coded-observations.csv"):
        return "coded_data"
    if path.endswith("/analysis.json"):
        return "analysis"
    if path.endswith("/law-updates.md"):
        return "correction_record"
    if path == "paper-b/provenance-matrix.csv":
        return "provenance"
    if path in {"paper-b/evidence-manifest.json", "paper-b/SHA256SUMS.json"}:
        return "integrity_manifest"
    return "release_metadata"


def release_metadata_files() -> list[BundleFile]:
    files: list[BundleFile] = []
    for source_path, bundle_path, role, rationale in RELEASE_METADATA:
        path = ROOT / source_path
        require(path.is_file(), f"release metadata source is missing: {source_path}")
        data = path.read_bytes().replace(b"\r\n", b"\n")
        files.append(
            BundleFile(
                bundle_path=bundle_path,
                data=data,
                source_repository="mibo-research-pilot/reports",
                source_commit=None,
                source_path=source_path,
                role=role,
                inclusion_rationale=rationale,
                source_state="release_candidate canonical Git text (CRLF-to-LF); final Git SHA recorded externally after merge",
            )
        )
    return files


def validate_release_metadata() -> None:
    lock = json.loads((ROOT / "paper-b" / "RELEASE_LOCK.json").read_text(encoding="utf-8"))
    require(lock.get("release_id") == RELEASE_ID and lock.get("release_version") == "1.0.0", "release identifier lock mismatch")
    require(lock.get("release_status") == "release_candidate", "release status must be release_candidate")
    require(lock.get("evidence_first_day") == 1 and lock.get("evidence_last_day") == 13, "release Day lock mismatch")
    require(lock.get("evidence_first_date") == "2026-05-05" and lock.get("evidence_last_date") == "2026-07-28", "release date lock mismatch")
    require(lock.get("included_observations") == 244 and lock.get("count_formula") == "12 + 12 + (11 * 20) = 244", "release observation-count lock mismatch")
    require(lock.get("collection_mode") == "api" and lock.get("api_collection_since") == "2026-05-05", "release API lock mismatch")
    require(lock.get("later_pilot_observations_included") is False, "later Pilot observations must be excluded")
    require(lock.get("query_instrument", {}).get("ordered_instrument_sha256") == INSTRUMENT_SHA, "release query hash lock mismatch")
    sources = lock.get("source_repositories", {})
    require(sources.get("core", {}).get("commit") == CORE_SHA, "release Core lock mismatch")
    require(sources.get("queries", {}).get("commit") == QUERIES_SHA, "release Queries lock mismatch")
    require(sources.get("reports", {}).get("evidence_source_commit") == REPORTS_EVIDENCE_SHA, "release Reports lock mismatch")

    source_metadata = json.loads((ROOT / "paper-b" / "release" / "SOURCE_REPOSITORIES.json").read_text(encoding="utf-8"))
    source_by_name = {entry.get("name"): entry for entry in source_metadata.get("repositories", [])}
    require(source_by_name.get("core", {}).get("pinned_source_sha") == CORE_SHA, "SOURCE_REPOSITORIES Core lock mismatch")
    require(source_by_name.get("queries", {}).get("pinned_source_sha") == QUERIES_SHA, "SOURCE_REPOSITORIES Queries lock mismatch")
    require(source_by_name.get("reports", {}).get("pinned_source_sha") == REPORTS_EVIDENCE_SHA, "SOURCE_REPOSITORIES Reports lock mismatch")


def repository_snapshot(repo: Path, commit: str, name: str, prefix: str) -> list[BundleFile]:
    classify = classify_core if name == "core" else classify_query
    role_text = "historical conceptual and methodological context" if name == "core" else "complete query-instrument provenance"
    return [
        BundleFile(
            bundle_path=f"{prefix}/{path}",
            data=git_blob(repo, commit, path),
            source_repository=f"mibo-research-pilot/{name}",
            source_commit=commit,
            source_path=path,
            role=classify(path),
            inclusion_rationale=f"Complete tracked pinned {name} snapshot preserving {role_text}.",
        )
        for path in tracked_paths(repo, commit)
    ]


def validate_query_instrument(query_repo: Path) -> None:
    instrument_bytes = git_blob(query_repo, QUERIES_SHA, "v0.1.1.json")
    hashes_bytes = git_blob(query_repo, QUERIES_SHA, "HASHES.json")
    instrument = load_json_bytes(instrument_bytes, "queries/v0.1.1.json")
    hashes = load_json_bytes(hashes_bytes, "queries/HASHES.json")
    queries = instrument.get("queries")
    require(instrument.get("query_count") == 5 and isinstance(queries, list) and len(queries) == 5, "query_count must be 5")
    ids = [entry.get("id") for entry in queries]
    require(ids == list(EXPECTED_QUERY_TEXTS) and len(ids) == len(set(ids)), "q001-q005 order or uniqueness changed")
    rows: list[str] = []
    hash_queries = hashes.get("queries")
    require(isinstance(hash_queries, dict) and set(hash_queries) == set(ids), "HASHES.json query IDs mismatch")
    for entry in queries:
        query_id = entry["id"]
        text = entry.get("text")
        require(text == EXPECTED_QUERY_TEXTS[query_id], f"exact query text changed: {query_id}")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        require(entry.get("exact_text_sha256") == digest, f"embedded query hash mismatch: {query_id}")
        require(hash_queries[query_id].get("text") == text, f"HASHES.json text mismatch: {query_id}")
        require(hash_queries[query_id].get("exact_text_sha256") == digest, f"HASHES.json hash mismatch: {query_id}")
        rows.append(f"{query_id}\t{entry['language']}\t{entry['category']}\t{text}\n")
    instrument_hash = hashlib.sha256("".join(rows).encode("utf-8")).hexdigest()
    require(instrument_hash == INSTRUMENT_SHA, "ordered instrument SHA-256 mismatch")
    require(instrument.get("instrument_content_sha256") == instrument_hash, "v0.1.1 instrument hash field mismatch")
    require(hashes.get("instrument_content_sha256") == instrument_hash, "HASHES.json instrument hash mismatch")


def reports_evidence_files() -> tuple[list[BundleFile], int]:
    manifest_data = git_blob(ROOT, REPORTS_EVIDENCE_SHA, "paper-b/evidence-manifest.json")
    hashes_data = git_blob(ROOT, REPORTS_EVIDENCE_SHA, "paper-b/SHA256SUMS.json")
    manifest = load_json_bytes(manifest_data, "reports/paper-b/evidence-manifest.json")
    hashes = load_json_bytes(hashes_data, "reports/paper-b/SHA256SUMS.json")

    included = manifest.get("included_days")
    require(isinstance(included, list), "reports evidence included_days must be a list")
    require([item.get("day") for item in included] == list(range(1, 14)), "reports evidence range must be Day 1-Day 13")
    counts = [item.get("expected_included_observations") for item in included]
    require(counts == [12, 12] + [20] * 11 and sum(counts) == 244, "independent observation count is not 244")
    require(manifest.get("total_included_observations") == 244, "reports evidence total is not 244")
    require(manifest.get("api_collection_since") == "2026-05-05" and manifest.get("collection_mode") == "api", "API collection lock mismatch")
    require({item.get("day") for item in manifest.get("excluded_later_pilot_observations", [])} == {14, 15}, "later Pilot exclusions mismatch")

    expected_schedule = {1: ["q001", "q002", "q003"], 2: ["q001", "q002", "q003"]}
    expected_schedule.update({day: list(EXPECTED_QUERY_TEXTS) for day in range(3, 14)})
    actual_schedule: dict[int, list[str]] = {}
    for period in manifest.get("query_schedule", []):
        for day in period.get("days", []):
            actual_schedule[day] = period.get("query_ids")
    require(actual_schedule == expected_schedule, "Paper B query schedule mismatch")

    selected = {"paper-b/README.md", "paper-b/evidence-manifest.json", "paper-b/provenance-matrix.csv"}
    for item in included:
        selected.add(item["report"])
        selected.update(item.get("additional_source_files", []))
    selected_paths = sorted(selected)
    hash_entries = hashes.get("files")
    require(isinstance(hash_entries, list), "existing reports SHA256SUMS files must be a list")
    require([item.get("path") for item in hash_entries] == selected_paths, "existing reports SHA file set is incompatible")
    require(len(selected_paths) == 21, "expected 21 existing reports evidence hash entries")

    files: list[BundleFile] = []
    for item in hash_entries:
        path = item["path"]
        data = git_blob(ROOT, REPORTS_EVIDENCE_SHA, path)
        canonical = data.replace(b"\r\n", b"\n")
        require(hashlib.sha256(canonical).hexdigest() == item.get("sha256"), f"existing reports evidence hash mismatch: {path}")
        files.append(
            BundleFile(
                bundle_path=f"reports-evidence/{path}",
                data=data,
                source_repository="mibo-research-pilot/reports",
                source_commit=REPORTS_EVIDENCE_SHA,
                source_path=path,
                role=classify_report(path),
                inclusion_rationale="Selected by the existing Paper B evidence manifest and verified by its SHA-256 manifest.",
            )
        )
    files.append(
        BundleFile(
            bundle_path="reports-evidence/paper-b/SHA256SUMS.json",
            data=hashes_data,
            source_repository="mibo-research-pilot/reports",
            source_commit=REPORTS_EVIDENCE_SHA,
            source_path="paper-b/SHA256SUMS.json",
            role="integrity_manifest",
            inclusion_rationale="Preserves the existing non-self-hashing integrity manifest for the Paper B reports evidence subset.",
        )
    )
    files.append(
        BundleFile(
            bundle_path="reports-evidence/LICENSE",
            data=git_blob(ROOT, REPORTS_EVIDENCE_SHA, "LICENSE"),
            source_repository="mibo-research-pilot/reports",
            source_commit=REPORTS_EVIDENCE_SHA,
            source_path="LICENSE",
            role="license_or_rights",
            inclusion_rationale="Preserves the pinned Reports source license as rights context; it is outside the unchanged 21-file Paper B evidence hash set and protected by the outer manifest.",
        )
    )
    return files, len(hash_entries)


def build_manifest(files: list[BundleFile]) -> bytes:
    entries = [
        {
            "bundle_path": item.bundle_path,
            "source_repository": item.source_repository,
            "source_commit": item.source_commit,
            "source_path": item.source_path,
            "source_state": item.source_state,
            "role": item.role,
            "sha256": item.sha256,
            "inclusion_rationale": item.inclusion_rationale,
        }
        for item in sorted(files, key=lambda value: value.bundle_path)
    ]
    return json_bytes(
        {
            "schema_version": "1.0",
            "release_id": RELEASE_ID,
            "release_status": "release_candidate",
            "algorithm": "SHA-256",
            "hashing_rule": "SHA-256 of exact bundle file bytes; no line-ending normalization",
            "enumerated_payload_file_count": len(entries),
            "final_bundle_file_count": len(entries) + 2,
            "self_reference_policy": "MANIFEST.json and outer SHA256SUMS.json are excluded from this payload enumeration to avoid circular hashes. The outer SHA256SUMS.json hashes MANIFEST.json and every other bundle file except itself.",
            "release_metadata_commit_policy": "Release-created files use source_commit null because the final release-preparation Git commit cannot self-embed. The final tag and GitHub Release metadata will record that commit after review and merge.",
            "files": entries,
        }
    )


def build_outer_hashes(files: list[BundleFile], manifest_data: bytes) -> bytes:
    hashes = {item.bundle_path: item.sha256 for item in files}
    hashes["MANIFEST.json"] = hashlib.sha256(manifest_data).hexdigest()
    entries = [{"path": path, "sha256": hashes[path]} for path in sorted(hashes)]
    return json_bytes(
        {
            "schema_version": "1.0",
            "release_id": RELEASE_ID,
            "algorithm": "SHA-256",
            "hashing_rule": "SHA-256 of exact bundle file bytes; no line-ending normalization",
            "hashed_file_count": len(entries),
            "final_bundle_file_count": len(entries) + 1,
            "self_hash_included": False,
            "scope_note": "This outer manifest covers the entire bundle, including MANIFEST.json, except for SHA256SUMS.json itself.",
            "files": entries,
        }
    )


def verify_or_write_metadata(manifest_data: bytes, outer_data: bytes, write: bool) -> None:
    expected = ((MANIFEST_SOURCE, manifest_data), (OUTER_HASH_SOURCE, outer_data))
    if write:
        for path, data in expected:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            print(f"WROTE: {path.relative_to(ROOT).as_posix()}")
        return
    for path, data in expected:
        require(path.is_file(), f"generated metadata is missing: {path.relative_to(ROOT)}")
        require(path.read_bytes() == data, f"generated metadata is stale: {path.relative_to(ROOT)}; rerun with --write-metadata")


def all_bundle_files(payload: list[BundleFile], manifest_data: bytes, outer_data: bytes) -> dict[str, bytes]:
    files = {item.bundle_path: item.data for item in payload}
    require(len(files) == len(payload), "duplicate bundle path")
    files["MANIFEST.json"] = manifest_data
    files["SHA256SUMS.json"] = outer_data
    return dict(sorted(files.items()))


def scan_sensitive(files: dict[str, bytes]) -> dict[str, list[str]]:
    secret_patterns = {
        "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "github_token": re.compile(r"\b(?:ghp|gho|github_pat)_[A-Za-z0-9_]{20,}\b"),
        "openai_style_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "bearer_token": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~-]{20,}"),
        "password_assignment": re.compile(r"(?i)\bpassword\s*[:=]\s*[\"']?[^\s\"']{8,}"),
    }
    local_path_patterns = (
        re.compile(r"(?i)\b[A-Z]:\\Users\\[^\s\"']+"),
        re.compile(r"(?i)(?:^|[\s\"'])/home/[^\s\"']+"),
        re.compile(r"(?i)(?:^|[\s\"'])/Users/[^\s\"']+"),
    )
    findings: dict[str, list[str]] = {name: [] for name in secret_patterns}
    findings["private_local_path"] = []
    findings["email_review"] = []
    email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
    for path, data in files.items():
        text = data.decode("utf-8", errors="ignore")
        for name, pattern in secret_patterns.items():
            if pattern.search(text):
                findings[name].append(path)
        if any(pattern.search(text) for pattern in local_path_patterns):
            findings["private_local_path"].append(path)
        if email_pattern.search(text):
            findings["email_review"].append(path)
    blocking = {name: paths for name, paths in findings.items() if name != "email_review" and paths}
    require(not blocking, f"potential secret or private local path found: {blocking}")
    return findings


def validate_bundle(files: dict[str, bytes], payload: list[BundleFile], reports_paths: set[str]) -> dict[str, list[str]]:
    require(all(not path.startswith("/") and "\\" not in path for path in files), "non-portable bundle path")
    require(all(".git" not in PurePosixPath(path).parts for path in files), ".git content found in bundle")
    require(".zenodo.json" not in files, ".zenodo.json must not be included")
    require(not any(path.startswith("reports-evidence/2026-08-") for path in files), "Day 14+ report evidence found in bundle")
    actual_reports = {path for path in files if path.startswith("reports-evidence/")}
    require(actual_reports == reports_paths, "reports evidence subset contains missing or extra paths")
    require(not any(item.source_repository.startswith("mibo-research/") for item in payload), "non-Pilot mibo-research source included")

    manifest = load_json_bytes(files["MANIFEST.json"], "bundle/MANIFEST.json")
    manifest_entries = manifest.get("files")
    require(isinstance(manifest_entries, list) and len(manifest_entries) == len(payload), "outer manifest payload count mismatch")
    for entry in manifest_entries:
        path = entry["bundle_path"]
        require(path in files, f"manifest path missing from bundle: {path}")
        require(hashlib.sha256(files[path]).hexdigest() == entry["sha256"], f"manifest hash mismatch: {path}")

    outer = load_json_bytes(files["SHA256SUMS.json"], "bundle/SHA256SUMS.json")
    outer_entries = outer.get("files")
    require(isinstance(outer_entries, list), "outer hash entries must be a list")
    expected_outer_paths = sorted(set(files) - {"SHA256SUMS.json"})
    require([entry.get("path") for entry in outer_entries] == expected_outer_paths, "outer hash file set is incomplete, extra, or unsorted")
    for entry in outer_entries:
        require(hashlib.sha256(files[entry["path"]]).hexdigest() == entry["sha256"], f"outer hash mismatch: {entry['path']}")

    release_metadata_text = "\n".join(
        files[path].decode("utf-8", errors="strict")
        for path in files
        if not path.startswith(("core-context/", "query-instrument/", "reports-evidence/"))
    )
    require(re.search(r"10\.\d{4,9}/\S+", release_metadata_text) is None, "DOI-like identifier found in release metadata")
    require(re.search(r"(?i)arxiv:\s*\d{4}\.\d{4,5}", release_metadata_text) is None, "arXiv identifier found in release metadata")
    require("release_status\": \"published" not in release_metadata_text, "release metadata calls candidate published")
    return scan_sensitive(files)


def write_tree(root: Path, files: dict[str, bytes]) -> None:
    for relative, data in files.items():
        target = root / PurePosixPath(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def write_zip(path: Path, files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED, strict_timestamps=True) as archive:
        for relative, data in sorted(files.items()):
            info = zipfile.ZipInfo(f"{BUNDLE_NAME}/{relative}", FIXED_ZIP_TIME)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            archive.writestr(info, data)


def remove_generated_tree(path: Path) -> None:
    """Remove only a validated generated output tree, including Windows read-only paths."""

    resolved = path.resolve()
    require(resolved != ROOT.resolve(), "refusing to remove repository root")

    def make_writable_and_retry(function: Any, target: str, _error: Any) -> None:
        os.chmod(target, stat.S_IWRITE)
        function(target)

    shutil.rmtree(resolved, onerror=make_writable_and_retry)


def deterministic_build(files: dict[str, bytes], dist_dir: Path) -> tuple[str, Path]:
    resolved_dist = dist_dir.resolve()
    require(resolved_dist == (ROOT / "dist").resolve(), "dist directory must resolve to the repository's generated dist/ path")
    with tempfile.TemporaryDirectory(prefix="mibo-paper-b-release-") as temporary:
        temp = Path(temporary)
        zip_one = temp / "one.zip"
        zip_two = temp / "two.zip"
        write_zip(zip_one, files)
        write_zip(zip_two, files)
        digest_one = hashlib.sha256(zip_one.read_bytes()).hexdigest()
        digest_two = hashlib.sha256(zip_two.read_bytes()).hexdigest()
        require(zip_one.read_bytes() == zip_two.read_bytes() and digest_one == digest_two, "deterministic ZIP verification failed")

        if resolved_dist.exists():
            remove_generated_tree(resolved_dist)
        resolved_dist.mkdir(parents=True)
        staging = resolved_dist / BUNDLE_NAME
        staging.mkdir()
        write_tree(staging, files)
        final_zip = resolved_dist / ZIP_NAME
        shutil.copyfile(zip_one, final_zip)
    return digest_one, final_zip


def collect_payload(core_repo: Path, queries_repo: Path) -> tuple[list[BundleFile], int, set[str]]:
    validate_release_metadata()
    verify_commit(ROOT, REPORTS_EVIDENCE_SHA, "mibo-research-pilot/reports")
    verify_commit(core_repo, CORE_SHA, "mibo-research-pilot/core")
    verify_commit(queries_repo, QUERIES_SHA, "mibo-research-pilot/queries")
    validate_query_instrument(queries_repo)

    report_files, existing_hash_count = reports_evidence_files()
    payload = release_metadata_files()
    payload.extend(repository_snapshot(core_repo, CORE_SHA, "core", "core-context"))
    payload.extend(repository_snapshot(queries_repo, QUERIES_SHA, "queries", "query-instrument"))
    payload.extend(report_files)
    paths = [item.bundle_path for item in payload]
    require(len(paths) == len(set(paths)), "duplicate payload path")
    report_paths = {item.bundle_path for item in report_files}
    return sorted(payload, key=lambda item: item.bundle_path), existing_hash_count, report_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-repo", type=Path, required=True, help="local Git repository containing the pinned Core commit")
    parser.add_argument("--queries-repo", type=Path, required=True, help="local Git repository containing the pinned Queries commit")
    parser.add_argument("--dist-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--write-metadata", action="store_true", help="regenerate committed MANIFEST.json and outer SHA256SUMS.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        payload, existing_hash_count, reports_paths = collect_payload(args.core_repo.resolve(), args.queries_repo.resolve())
        manifest_data = build_manifest(payload)
        outer_data = build_outer_hashes(payload, manifest_data)
        verify_or_write_metadata(manifest_data, outer_data, args.write_metadata)
        files = all_bundle_files(payload, manifest_data, outer_data)
        findings = validate_bundle(files, payload, reports_paths)
        zip_sha, zip_path = deterministic_build(files, args.dist_dir)
        summary = {
            "release_id": RELEASE_ID,
            "release_status": "release_candidate",
            "bundle_file_count": len(files),
            "manifest_payload_file_count": len(payload),
            "outer_hashed_file_count": len(files) - 1,
            "existing_reports_evidence_hash_count": existing_hash_count,
            "observation_count": 244,
            "instrument_sha256": INSTRUMENT_SHA,
            "zip_path": zip_path.name,
            "zip_sha256": zip_sha,
            "outer_manifest_sha256": hashlib.sha256(outer_data).hexdigest(),
            "deterministic_build": "pass; two byte-identical ZIP builds",
            "secret_scan": "pass; no blocking secret or private local path pattern found",
            "email_review_paths": findings["email_review"],
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
