# Model selection correction for the thirteen wave Pilot

Correction date: 11 October 2026

The investigator has confirmed that model selection was unchanged during the 13 included waves and has instructed that the initial collector configuration be used as the correct model notation. This correction applies to the selected models for Day 1–Day 13, 5 May–28 July 2026 (Asia/Tokyo), comprising 244 recorded responses.

| Service | Corrected selected API model ID |
|---|---|
| OpenAI ChatGPT | `gpt-5.5` |
| Anthropic Claude | `claude-opus-4-8` |
| Google Gemini | `gemini-3.5-flash` |
| Perplexity | `sonar` |

The canonical source is the [initial collector configuration at commit aeddf8ef](https://github.com/mibo-research-pilot/reports/blob/aeddf8ef53b99a4e0667ed2c56ce00bd6cc30d49/scripts/observation_config.json). All five retained configuration revisions preserve these four observation-model IDs. The investigator described the selection as models commonly used at the time. This is a pragmatic selection rationale, not a measured popularity ranking or a probability sample of services.

Earlier report headers naming GPT-5.4, Claude Opus 4.7, or Gemini 3.0 Flash, and the nonspecific Perplexity Web Search label, are superseded model metadata. They remain in the historical artifacts so that the correction can be traced. Header differences do not establish a model-switch event. The machine-readable correction is [model-selection.json](./model-selection.json).

For Perplexity, `sonar` is the selected Sonar API model ID. The retained collector uses the Perplexity chat/completions endpoint. Later August metadata also records `sonar`; those later responses do not enter the 244-response Paper B corpus. The API model ID does not identify an immutable internal weight snapshot or prove what source passages supported each answer.

The first retained configuration commit is timestamped 28 July 2026 at 16:10:09 UTC, or 29 July at 01:10:09 in Asia/Tokyo. It therefore postdates the final declared observation date. The historical model-selection assignment is an investigator-confirmed metadata correction; it is not independent authentication of every earlier API transaction. Incomplete original requests, capture times, retrieval settings, and response preservation remain limitations.

This correction changes model metadata and its interpretation. It preserves the historical response texts, query wording, counts, source ledgers, coding, and corrections. The published `paper-b-pilot-evidence-v1.0.0` release remains unchanged; readers of that release should also consult this later correction. The live evidence manifest and its hashes are updated for the intentionally revised documentation.
