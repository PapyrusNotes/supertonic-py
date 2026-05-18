# supertonic serve

Run a thin local HTTP server around the same TTS engine. Exposes a native
`/v1/*` namespace plus an **OpenAI Audio Speech-compatible alias** so any
client that already speaks the OpenAI API can swap the base URL.

!!! note "Requires `fastapi` + `uvicorn`"
    Install with: `pip install 'supertonic[serve]'`

## Usage

```bash
supertonic serve [--host HOST] [--port PORT] [OPTIONS]
```

Default bind is `127.0.0.1:7788`. Binding to any other interface is opt-in
and emits a one-line stderr warning — put the server behind a reverse proxy
when exposing it beyond loopback.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/v1/health` | Liveness/readiness, returns `{status, model, sample_rate, version, voices_loaded}` |
| `GET`  | `/v1/styles` | List built-in voices + imported custom voices |
| `POST` | `/v1/styles/import` | Upload a Voice Builder JSON (multipart or JSON body); persisted per-model under `~/.cache/<model>/custom_styles/` |
| `POST` | `/v1/tts` | Native synthesis — full Supertonic parameter set |
| `POST` | `/v1/audio/speech` | OpenAI-compatible alias for `/v1/tts` |
| `POST` | `/v1/tts/batch` | Synthesize up to 64 items in one request (JSON + base64) |

Interactive OpenAPI docs are served at `/docs` when the process is running.

## Quick examples

```bash
# Native endpoint
curl -X POST http://127.0.0.1:7788/v1/tts \
  -H 'content-type: application/json' \
  -d '{"text":"Supertonic is a lightning fast, on-device TTS system.","voice":"M1","lang":"en"}' \
  -o output.wav

# OpenAI-compatible alias — base-URL swap is enough for OpenAI SDK clients
curl -X POST http://127.0.0.1:7788/v1/audio/speech \
  -H 'content-type: application/json' \
  -d '{"model":"supertonic-3","input":"Hello in my own cloned voice.","voice":"M1","response_format":"wav"}' \
  -o output.wav

# Import a Voice Builder export, then synthesize with it
curl -X POST http://127.0.0.1:7788/v1/styles/import -F "file=@voices/my_voice.json"
curl -X POST http://127.0.0.1:7788/v1/tts \
  -H 'content-type: application/json' \
  -d '{"text":"Hello in my own cloned voice.","voice":"my_voice","lang":"en"}' \
  -o output_own_voice.wav
```

See the [Local Server section in Quick Start](../quickstart.md#local-server)
for the full walkthrough (Voice Builder import, batch, response formats).

## Audio output formats

Supported `response_format` values: `wav` (default), `flac`, `ogg`
(Vorbis). MP3, AAC, and Opus are intentionally not supported in v1 — Opus
because libsndfile's OPUS encoder is fixed to 8/12/16/24/48 kHz while the
model is 44.1 kHz; MP3/AAC because they would add encoder dependencies.
Clients should pick one of the supported formats or transcode externally.

## Errors

Every error response uses the OpenAI-shaped envelope so existing error
parsers in OpenAI SDK clients continue to work:

```json
{
  "error": {
    "message": "unsupported response_format 'mp3'; set response_format to one of: wav, flac, ogg",
    "type": "invalid_request_error",
    "code": "unsupported_response_format"
  }
}
```

Common codes:

* synthesis: `unknown_voice`, `unsupported_lang`, `unsupported_response_format`,
  `unknown_model`, `model_not_loaded`, `synthesis_failed`, `not_ready`
* style import: `style_name_conflict`, `invalid_style_name`,
  `invalid_style_payload`, `missing_file`, `missing_name`, `invalid_json`,
  `invalid_body`
* request size: `payload_too_large`, `invalid_content_length` (from the
  `Content-Length` pre-flight middleware on `POST /v1/styles/import`)

## Arguments

--8<-- "docs/argparse/serve.inc.md"
