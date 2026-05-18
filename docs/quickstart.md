# Quick Start

<figure markdown="block">
<video src="../assets/video/supertonic-pip-demo-low.mp4" autoplay loop muted playsinline controls style="width: 100%; max-width: 100%; border-radius: 8px;"></video>
</figure>

## Installation

```bash
pip install supertonic
```

## Basic Usage

=== "Python"

    ```python
    from supertonic import TTS

    # Note: First run downloads model automatically (~400MB)
    tts = TTS(auto_download=True)

    # Get a voice style (10 built-in: M1–M5, F1–F5)
    style = tts.get_voice_style(voice_name="F3")

    # Generate speech. `lang` is optional — Supertonic-3 auto-resolves to
    # the "na" fallback (so unknown text just works); pass an ISO code to
    # opt into language-specific handling.
    text = "The train delay was announced at 4:45 PM on Wed, Apr 3, 2024 due to track maintenance."
    wav, duration = tts.synthesize(text, voice_style=style, lang="en")
    # wav: np.ndarray, shape = (1, num_samples)
    # duration: np.ndarray, shape = (1,)

    # Save to file
    tts.save_audio(wav, "output.wav")
    ```

    ??? tip "Arguments for `tts.synthesize()`"
        | Parameter | Description | Default |
        |-----------|-------------|---------|
        | `text` | Text to synthesize | *required* |
        | `voice_style` | Voice style object | *required* |
        | `lang` | Language code (Supertonic-3: 31 codes + `na` fallback). See [Multilingual Support](#multilingual-support). | auto (`na` for v2/v3, `en` for v1) |
        | `total_steps` | Quality: 5-12 typical (higher=better) | `8` |
        | `speed` | Speed: 0.7 (slow) to 2.0 (fast) | `1.05` |
        | `max_chunk_length` | Max characters per chunk | `300` |
        | `silence_duration` | Silence between chunks (seconds) | `0.3` |
        | `verbose` | Show detailed progress | `False` |

    ??? tip "Shorthand"
        Use `tts(...)` as shorthand for `tts.synthesize(...)`:
        ```python
        wav, duration = tts("This is a convenient shorthand method.", voice_style=style)
        ```

=== "CLI"

    ```bash
    # Note: First run downloads model automatically (~400MB)
    supertonic tts 'Supertonic is a lightning fast, on-device TTS system.' -o output.wav

    # Multilingual support
    supertonic tts '회의는 2024년 4월 3일 수요일 오후 4시 45분에 시작됩니다.' -o korean.wav --lang ko
    ```

    ??? tip "CLI Options"
        | Option | Description | Default |
        |--------|-------------|---------|
        | `-o`, `--output` | Output file path | *required* |
        | `--voice` | Voice style: M1–M5, F1–F5 (10 built-in) | `M1` |
        | `--lang` | Language (Supertonic-3: 31 codes + `na` fallback). See [Multilingual Support](#multilingual-support). | auto (`na` for v2/v3, `en` for v1) |
        | `--steps` | Quality steps: 5-12 typical | `8` |
        | `--speed` | Speed multiplier: 0.7-2.0 | `1.05` |
        | `--max-chunk-length` | Characters per chunk | `300` |
        | `--silence-duration` | Silence between chunks (seconds) | `0.3` |
        | `--custom-style-path` | Path to custom voice style JSON | - |
        | `-v`, `--verbose` | Show detailed progress | `False` |

    ??? tip "Utility Commands"
        ```bash
        supertonic list-voices   # List available voices
        supertonic info          # Show model information
        supertonic version       # Show version
        ```

---

## Try in Colab

Run and experiment with Supertonic in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/supertone-inc/supertonic-py/blob/main/notebook/supertonic_demo.ipynb)

---

## Advanced Usage

### Multilingual Support

Supertonic-3 supports **31 languages** with natural text handling, plus a special `na` fallback for unknown / unsupported languages.

=== "Supported codes"

    | Code | Language | Code | Language | Code | Language | Code | Language |
    |------|----------|------|----------|------|----------|------|----------|
    | `en` | English | `ko` | Korean | `ja` | Japanese | `ar` | Arabic |
    | `bg` | Bulgarian | `cs` | Czech | `da` | Danish | `de` | German |
    | `el` | Greek | `es` | Spanish | `et` | Estonian | `fi` | Finnish |
    | `fr` | French | `hi` | Hindi | `hr` | Croatian | `hu` | Hungarian |
    | `id` | Indonesian | `it` | Italian | `lt` | Lithuanian | `lv` | Latvian |
    | `nl` | Dutch | `pl` | Polish | `pt` | Portuguese | `ro` | Romanian |
    | `ru` | Russian | `sk` | Slovak | `sl` | Slovenian | `sv` | Swedish |
    | `tr` | Turkish | `uk` | Ukrainian | `vi` | Vietnamese | `na` | *unknown / fallback* |

=== "Python"

    ```python
    from supertonic import TTS

    tts = TTS()
    style = tts.get_voice_style("M1")

    # English
    wav_en, _ = tts.synthesize("Hello, welcome to Supertonic!", voice_style=style, lang="en")

    # Korean
    wav_ko, _ = tts.synthesize("안녕하세요! 수퍼토닉에 오신 것을 환영합니다.", voice_style=style, lang="ko")

    # Japanese
    wav_ja, _ = tts.synthesize("こんにちは！スーパートニックへようこそ。", voice_style=style, lang="ja")

    # German
    wav_de, _ = tts.synthesize("Hallo! Willkommen bei Supertonic.", voice_style=style, lang="de")

    # Unknown language fallback — wraps text with the <na> token
    wav_na, _ = tts.synthesize("Some uncommon text.", voice_style=style, lang="na")

    tts.save_audio(wav_ko, "output_korean.wav")
    ```

=== "CLI"

    ```bash
    # English
    supertonic tts 'Hello, welcome to Supertonic!' -o output_en.wav

    # Korean
    supertonic tts '안녕하세요! 수퍼토닉에 오신 것을 환영합니다.' --lang ko -o output_ko.wav

    # Japanese
    supertonic tts 'こんにちは！スーパートニックへようこそ。' --lang ja -o output_ja.wav

    # German
    supertonic tts 'Hallo! Willkommen bei Supertonic.' --lang de -o output_de.wav

    # Unknown language fallback
    supertonic tts 'Some uncommon text.' --lang na -o output_na.wav
    ```

---

### Voice Styles

Supertonic provides multiple built-in voice styles to choose from:

=== "Python"

    ```python
    from supertonic import TTS

    tts = TTS()

    # List available voices (10 built-in: M1–M5, F1–F5)
    voice_list = tts.voice_style_names

    # Try different voices
    for voice_name in voice_list:
        style = tts.get_voice_style(voice_name)
        wav, dur = tts.synthesize(f"This is the {voice_name} voice style demonstration.", voice_style=style)
        tts.save_audio(wav, f"output_{voice_name}.wav")
    ```

=== "CLI"

    ```bash
    # List available voices
    supertonic list-voices

    # Try different voices
    supertonic tts 'This is the M1 voice style demonstration.' --voice M1 -o output_m1.wav
    supertonic tts 'This is the M2 voice style demonstration.' --voice M2 -o output_m2.wav
    supertonic tts 'This is the F1 voice style demonstration.' --voice F1 -o output_f1.wav
    supertonic tts 'This is the F2 voice style demonstration.' --voice F2 -o output_f2.wav
    ```

#### Custom Voice Styles

Load custom voice styles from JSON:

=== "Python"

    ```python
    from supertonic import TTS
    from pathlib import Path

    tts = TTS()

    # Load custom style from JSON
    custom_style = tts.get_voice_style_from_path(Path("custom_voice.json"))
    wav, dur = tts.synthesize("Using a custom voice style from JSON file.", voice_style=custom_style)
    ```

=== "CLI"

    ```bash
    supertonic tts 'Using a custom voice style from JSON file.' --custom-style-path custom_voice.json -o output_custom.wav
    ```

---

## Local Server

`supertonic serve` runs a thin local HTTP wrapper around the same engine —
useful when embedding a Python interpreter is awkward (n8n community nodes,
browser extensions, Electron apps, Unity, Home Assistant, robotics devices,
or anything that already speaks the OpenAI Audio Speech API).

### Install and run

```bash
pip install 'supertonic[serve]'                    # adds fastapi + uvicorn
supertonic serve --host 127.0.0.1 --port 7788      # defaults; loopback only
```

Once it's up:

- Native synthesis endpoint: `http://127.0.0.1:7788/v1/tts`
- OpenAI-compatible alias: `http://127.0.0.1:7788/v1/audio/speech`
- Interactive OpenAPI docs: `http://127.0.0.1:7788/docs`

!!! note "Binding beyond loopback"
    `--host` defaults to `127.0.0.1`. Anything else is opt-in and emits a
    one-line warning — put the server behind a reverse proxy if you do.

### Generate audio

=== "Native API"

    Full Supertonic parameter set (`steps`, `max_chunk_length`,
    `silence_duration`, …):

    ```bash
    curl -X POST http://127.0.0.1:7788/v1/tts \
      -H 'content-type: application/json' \
      -d '{
            "text": "Supertonic is a lightning fast, on-device TTS system.",
            "voice": "M1",
            "lang": "en",
            "steps": 8,
            "speed": 1.05,
            "response_format": "wav"
          }' \
      -o output.wav
    ```

    Response is the raw audio bytes (`audio/wav` by default). Useful
    response headers: `X-Audio-Duration` (seconds), `X-Sample-Rate`, and
    `X-Supertonic-Version`. Supported `response_format` values: `wav`,
    `flac`, `ogg` (Vorbis).

=== "OpenAI-compatible"

    Clients that already speak the OpenAI Audio Speech API only need to
    swap the base URL:

    ```bash
    curl -X POST http://127.0.0.1:7788/v1/audio/speech \
      -H 'content-type: application/json' \
      -d '{
            "model": "supertonic-3",
            "input": "Supertonic is a lightning fast, on-device TTS system.",
            "voice": "M1",
            "response_format": "wav"
          }' \
      -o output.wav
    ```

    Multilingual input works the same way — just set `lang` to any code from
    [Multilingual Support](#multilingual-support) (or `na` for the fallback).

### Custom voices (Voice Builder JSON)

A voice JSON exported from
[Voice Builder](https://supertonic.supertone.ai/voice_builder) (or any of
the bundled `~/.cache/supertonic3/voice_styles/*.json` files) can be
uploaded once and referenced by name on every subsequent request.

=== "Import"

    ```bash
    # multipart upload — the filename stem becomes the voice name
    curl -X POST http://127.0.0.1:7788/v1/styles/import \
      -F "file=@voices/my_voice.json"
    # → {"name":"my_voice","stored_at":"~/.cache/supertonic3/custom_styles/my_voice.json"}

    # override the name; allow overwriting an existing entry
    curl -X POST "http://127.0.0.1:7788/v1/styles/import?overwrite=true" \
      -F "file=@voices/my_voice.json" \
      -F "name=demo_voice"

    # or send a JSON body directly (handy from scripts / n8n)
    curl -X POST http://127.0.0.1:7788/v1/styles/import \
      -H 'content-type: application/json' \
      -d '{"name":"demo_voice","style_ttl":{...},"style_dp":{...}}'
    ```

=== "Synthesize"

    ```bash
    curl -X POST http://127.0.0.1:7788/v1/tts \
      -H 'content-type: application/json' \
      -d '{"text":"Hello in my own cloned voice.","voice":"my_voice","lang":"en"}' \
      -o output_own_voice.wav
    ```

!!! info "Per-model storage"
    Imported voices are persisted **per model** alongside the bundled voice
    styles — e.g. `~/.cache/supertonic3/custom_styles/<name>.json` for
    `supertonic-3`, `~/.cache/supertonic2/custom_styles/<name>.json` for
    `supertonic-2`. They are re-loaded automatically on the next
    `supertonic serve` start. Names that collide with the built-ins
    (`M1`–`M5`, `F1`–`F5`) are rejected; existing custom names return `409`
    unless you pass `?overwrite=true`. `GET /v1/styles` lists everything
    available for the loaded model.

### Batch synthesis

`POST /v1/tts/batch` accepts up to 64 items in a single request and returns
each result as base64-encoded audio. Per-item `voice` / `lang` / `speed` can
differ — useful for narration jobs that mix speakers or languages.

```bash
curl -X POST http://127.0.0.1:7788/v1/tts/batch \
  -H 'content-type: application/json' \
  -d '{
        "items": [
          {"text": "Supertonic is a lightning fast, on-device TTS system.", "voice": "M1", "lang": "en"},
          {"text": "회의는 잠시 후에 시작되며 모두가 자리에 앉아 기다립니다.", "voice": "F1", "lang": "ko"},
          {"text": "La reunión comienza pronto y todos se sientan en silencio para escuchar.", "voice": "F1", "lang": "es"}
        ],
        "response_format": "wav",
        "defaults": {"steps": 8, "speed": 1.05}
      }'
```

The response is a JSON object with an `items` array:

```json
{
  "items": [
    {"audio_base64": "...", "duration_s": 4.32, "format": "wav", "sample_rate": 44100},
    {"audio_base64": "...", "duration_s": 4.88, "format": "wav", "sample_rate": 44100},
    {"audio_base64": "...", "duration_s": 5.36, "format": "wav", "sample_rate": 44100}
  ]
}
```

Each item carries fully self-contained audio bytes, so writing them out is
a one-liner:

```bash
curl -fsS -X POST http://127.0.0.1:7788/v1/tts/batch \
  -H 'content-type: application/json' \
  -d '@payload.json' \
| python3 -c '
import sys, json, base64, pathlib
for i, item in enumerate(json.load(sys.stdin)["items"]):
    pathlib.Path(f"batch_{i}.wav").write_bytes(base64.b64decode(item["audio_base64"]))
'
```

!!! note "Sequential, not parallel"
    Items are processed sequentially within a process (the ONNX session is
    serialized) — so batching saves HTTP round-trips and packages related
    work together, not raw inference time. Any per-item failure returns a
    `400` with `items[<index>]` in the error message; no audio is emitted
    partially.

See also: **[supertonic serve](cli/serve.md)** for full CLI flags and
**[supertonic.server](api/server.md)** for embedding the FastAPI app in a
larger ASGI service.

---

### Speech Speed Control

Adjust speech rate from 0.7× (slow) to 2.0× (fast):

| Speed | Description |
|-------|-------------|
| `0.7` | Slow pace |
| `1.0` | Normal pace |
| `1.3` | Faster pace |
| `2.0` | Fast pace |

=== "Python"

    ```python
    from supertonic import TTS

    tts = TTS()
    style = tts.get_voice_style("F1")

    texts = {
        0.7: "This is slow speed demonstration.",
        1.0: "This is normal speed demonstration.",
        1.3: "This is fast speed demonstration.",
        2.0: "This is fastest speed demonstration.",
    }

    for speed, text in texts.items():
        wav, dur = tts.synthesize(text, voice_style=style, speed=speed)
        tts.save_audio(wav, f"output_{speed:.1f}_speed.wav")
    ```

=== "CLI"

    ```bash
    supertonic tts 'This is slow speed demonstration.' --voice F1 --speed 0.7 -o output_0.7_speed.wav
    supertonic tts 'This is normal speed demonstration.' --voice F1 --speed 1.0 -o output_1.0_speed.wav
    supertonic tts 'This is fast speed demonstration.' --voice F1 --speed 1.3 -o output_1.3_speed.wav
    supertonic tts 'This is fastest speed demonstration.' --voice F1 --speed 2.0 -o output_2.0_speed.wav
    ```

### Speech Quality Control

Adjust synthesis quality with `total_steps` parameter:

| Steps | Quality | Synthesis Speed |
|-------|---------|-----------------|
| `2` | Low | Fast |
| `5` | Balanced | Normal |
| `10` | High | Slow |

=== "Python"

    ```python
    from supertonic import TTS

    tts = TTS()
    style = tts.get_voice_style("M1")

    texts = {
        2: "This is low steps demonstration.",
        5: "This is balanced steps demonstration.",
        10: "This is high steps demonstration.",
    }

    for steps, text in texts.items():
        wav, dur = tts.synthesize(text, voice_style=style, total_steps=steps)
        tts.save_audio(wav, f"output_{steps:02d}_steps.wav")
    ```

=== "CLI"

    ```bash
    supertonic tts 'This is low steps demonstration.' --steps 2 -o output_02_steps.wav
    supertonic tts 'This is balanced steps demonstration.' --steps 5 -o output_05_steps.wav
    supertonic tts 'This is high steps demonstration.' --steps 10 -o output_10_steps.wav
    ```

### Long Text Handling

Supertonic automatically chunks long texts for optimal processing:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `max_chunk_length` | Maximum characters per chunk | `300` |
| `silence_duration` | Silence between chunks (seconds) | `0.3` |

=== "Python"

    ```python
    from supertonic import TTS

    tts = TTS()
    style = tts.get_voice_style("F1")

    long_text = """
    Artificial intelligence has transformed many fields.
    From healthcare to transportation, AI systems are making impacts.
    Natural language processing allows computers to understand human language.
    These advances are opening up new possibilities.
    """

    wav, dur = tts.synthesize(
        long_text,
        voice_style=style,
        max_chunk_length=300,
        silence_duration=0.3
    )
    tts.save_audio(wav, "output.wav")
    ```

=== "CLI"

    ```bash
    TEXT="Artificial intelligence has transformed many fields. From healthcare to transportation, AI systems are making impacts. Natural language processing allows computers to understand human language. These advances are opening up new possibilities."

    supertonic tts "$TEXT" --max-chunk-length 150 --silence-duration 0.3 --voice F1 -o output.wav  # Note: Use double quotes for shell variables
    ```

!!! info "Auto-chunking"
    Text chunking is enabled by default. Supertonic splits by paragraphs and respects sentence boundaries, handling abbreviations like Mr., Dr., Ph.D. correctly.

### Text Validation

Check if your text can be processed before synthesis:

=== "Python"

    ```python
    from supertonic import TTS

    tts = TTS()
    text_processor = tts.model.text_processor

    # Check if text is supported
    text = "Hello World! Welcome to 世界."
    is_valid, unsupported = text_processor.validate_text(text)

    if not is_valid:
        print(f"Unsupported characters: {unsupported}")
        # Will show: ['世', '界'] (or similar)

    # Get all supported characters
    supported_chars = text_processor.supported_character_set
    print(f"Supported characters: {sorted(list(supported_chars))}")
    ```

=== "CLI"

    ```bash
    # This will output an error because the text contains unsupported characters
    supertonic tts 'Hello World! Welcome to 世界.' -o output.wav
    ```


---

## Performance Tuning

### Thread Configuration

By default, ONNX Runtime automatically detects and uses optimal thread counts for your system. For advanced use cases, you can manually configure threads:

| Parameter | Description |
|-----------|-------------|
| `intra_op_num_threads` | Threads for parallelism within each operation |
| `inter_op_num_threads` | Threads for parallelism between operations |

=== "Python"

    ```python
    from supertonic import TTS

    # Auto-detect (recommended)
    tts = TTS()

    # High-performance server
    tts = TTS(intra_op_num_threads=12, inter_op_num_threads=12)

    # Low-resource environment
    tts = TTS(intra_op_num_threads=2, inter_op_num_threads=2)
    ```

=== "CLI"

    ```bash
    # Set thread counts via environment variables
    export SUPERTONIC_INTRA_OP_THREADS=12
    export SUPERTONIC_INTER_OP_THREADS=12

    supertonic tts 'This is the thread configuration demonstration.' -o output.wav --voice M1
    ```

---

## Next Steps

- **[API Reference](api/index.md)** — Complete API documentation
- **[CLI Reference](cli/README.md)** — Full command-line interface guide
