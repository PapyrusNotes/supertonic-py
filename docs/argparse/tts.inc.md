#### `TEXT`

Text to synthesize

#### `-o`, `--output`

Output WAV file

#### `--model`

Possible choices: `supertonic`, `supertonic-2`

Model to use: supertonic (English only) or supertonic-2 (multilingual). Default: supertonic-2

Default: `supertonic-2`

#### `--voice`

Voice style (default: M1)

Default: `M1`

#### `--custom-style-path`

Path to custom voice style JSON file (overrides --voice if provided)

#### `--lang`

Possible choices: `en`, `ko`, `es`, `pt`, `fr`

Language code: en (English), ko (Korean), es (Spanish), pt (Portuguese), fr (French). Default: en

Default: `en`

#### `--steps`

Quality steps (default: 5, higher=better)

Default: `5`

#### `--speed`

Speech speed (0.7-2.0, default: 1.05, 2.0=2x faster)

Default: `1.05`

#### `--max-chunk-length`

Maximum characters per chunk (default: auto based on language)

#### `--silence-duration`

Silence between chunks in seconds (default: 0.3)

Default: `0.3`

#### `-v`, `--verbose`

Enable verbose output with detailed logging

Default: `False`

