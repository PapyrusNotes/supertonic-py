# Changelog

All notable changes to **supertonic-py** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project broadly follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html);
**see the heads-up note below 1.2.2 — that release carries default-value
shifts in `total_steps` and `lang` that are semver-minor in nature but are
shipping under a patch bump on purpose.**

## [1.2.2] — Unreleased

### Heads-up — soft behavior changes in this patch

This release intentionally changes the **default value** of two public
parameters. Code copy-pasted from older docs or tutorials will keep
working, but the audio it produces will be subtly different.

- `TTS.synthesize(total_steps=...)` default `5` → `8`. Output quality
  goes up; synthesis is slightly slower. To keep the old behavior, pass
  `total_steps=5` explicitly.
- `TTS.synthesize(lang=...)` default no longer hard-coded to `"en"`.
  When unset, supertonic-2 / supertonic-3 now resolve to the language-
  agnostic `"na"` fallback (so non-English text "just works" without the
  user picking a code), and supertonic v1 still resolves to `"en"`. To
  keep the old behavior on v3, pass `lang="en"` explicitly.

### Added
- `MODEL_CONFIGS` entries now pin the Hugging Face Hub revision SHA per
  model. `pip install supertonic==1.2.2` will always download the same
  ONNX weights, even if the upstream HF repos are updated later. The
  pinned SHAs:
  - `Supertone/supertonic` → `b6856d033f622c63ea29441795be266a1133e227`
  - `Supertone/supertonic-2` → `75e6727618a02f323c720cba9478152d4bc16ca4`
  - `Supertone/supertonic-3` → `724fb5abbf5502583fb520898d45929e62f02c0b`
- `supertonic.config.get_model_revision(model_name)` helper; the
  `SUPERTONIC_MODEL_REVISION` env var continues to act as a manual
  override (primarily for development).
- `SECURITY.md` with a responsible-disclosure contact.
- `CHANGELOG.md` (this file).

### Changed
- **Default `total_steps`** raised from `5` to `8`
  (`supertonic/config.py:DEFAULT_TOTAL_STEPS`). Affects
  `TTS.synthesize`, `TTS.__call__`, and the `--steps` CLI option.
- **Default `lang`** is now model-aware. The `synthesize` /  `__call__`
  signatures changed from `lang: str = "en"` to
  `lang: Optional[str] = None`. When `None`, the value is resolved at
  synthesis time:
  - Multilingual models (supertonic-2 / supertonic-3) → `"na"` fallback
  - English-only supertonic v1 → `"en"`
- CLI `--lang` default also becomes `None`; `--help` now reads
  *"Default: 'na' for multilingual models (supertonic-2/3), 'en' for
  supertonic v1."*
- Model download size reference updated from `~305 MB` to `~400 MB`
  across README and docs.
- README and `docs/index.md` restructured: Python Quick Start moved
  above CLI, the snippet annotated inline so it doubles as
  copy-paste-to-an-LLM documentation, new "Custom voices (Voice
  Builder)" subsection covers `get_voice_style_from_path()` and the
  `~/.cache/supertonic3/voice_styles/{M1..M5,F1..F5}.json` layout.
- Documentation now consistently states there are **10 built-in voices**
  (M1–M5, F1–F5) — previously some surfaces said only four.
- `docs/quickstart.md`, `docs/api/index.md`, `docs/cli/README.md`,
  `supertonic/__init__.py` example, and the `get_voice_style()`
  docstring updated to match the new defaults.

### Fixed
- `cli.py` first-run progress line no longer prints `lang=None` when
  the language is unspecified; shows `lang=auto` instead.
- `examples/test2_voices.py` docstring now accurately reflects the
  full 10-voice set the script iterates over.

## [1.2.1] — Unreleased

`1.2.1` was bumped in source but never tagged. Its work has been folded
into `1.2.2`. Notable items from that interim:

- **feat**: Supertonic-3 multilingual support (31 ISO languages plus
  `"na"` fallback for unknown / unsupported text). Adds the new
  `Supertone/supertonic-3` HF Hub repo and corresponding entries in
  `MODEL_CONFIGS`. Commit `9d5373d`.
- **fix**: preserve diacritics in text preprocessing. Commit `d02b8b5`.
- **chore**: package authors updated. Commit `074eca5`.

## [1.2.0] — 2026-01-24

- Documentation refresh: multilingual section in quickstart, new banner
  image, README links pointing to raw GitHub for image assets, license
  format normalized in metadata. Commits `87ed50a`, `7f35d03`,
  `db57854`, `0f473a0`.

## [1.1.2] — 2026-01-24

- Banner URL fix and patch bump. Commit `1e3e202`. Banner image and
  URLs updated for supertonic-2. Commit `5a8eeae`.

## [1.1.1] — 2026-01-24

- First multilingual release (`supertonic-2`). Commit `ef1c39f`.

## [1.0.0] — 2025-11-24 → 2025-12-10

- Initial public release: English-only supertonic v1 on ONNX Runtime,
  HF Hub model download, CLI (`supertonic say` / `tts` / `list-voices`
  / `info`), 10 built-in voices.

[1.2.2]: https://github.com/supertone-inc/supertonic-py/compare/v1.2.0...v1.2.2
[1.2.1]: https://github.com/supertone-inc/supertonic-py/compare/v1.2.0...v1.2.2
[1.2.0]: https://github.com/supertone-inc/supertonic-py/compare/v1.1.2...v1.2.0
[1.1.2]: https://github.com/supertone-inc/supertonic-py/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/supertone-inc/supertonic-py/compare/v1.0.0...v1.1.1
[1.0.0]: https://github.com/supertone-inc/supertonic-py/releases/tag/v1.0.0
