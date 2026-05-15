#### `TEXT`

Text to synthesize and play

#### `--model`

Possible choices: `supertonic`, `supertonic-2`, `supertonic-3`

Model to use: supertonic (English only), supertonic-2 (5 languages), or supertonic-3 (31 languages + 'na' fallback). Default: supertonic-3

Default: `supertonic-3`

#### `--voice`

Voice style (default: M1)

Default: `M1`

#### `--custom-style-path`

Path to custom voice style JSON file (overrides --voice if provided)

#### `--lang`

Possible choices: `en`, `ko`, `ja`, `ar`, `bg`, `cs`, `da`, `de`, `el`, `es`, `et`, `fi`, `fr`, `hi`, `hr`, `hu`, `id`, `it`, `lt`, `lv`, `nl`, `pl`, `pt`, `ro`, `ru`, `sk`, `sl`, `sv`, `tr`, `uk`, `vi`, `na`

Language code (supertonic-3): en, ko, ja, ar, bg, cs, da, de, el, es, et, fi, fr, hi, hr, hu, id, it, lt, lv, nl, pl, pt, ro, ru, sk, sl, sv, tr, uk, vi, or 'na' for unknown / unsupported languages. Default: 'na' for multilingual models (supertonic-2/3), 'en' for supertonic v1.

#### `--steps`

Quality steps (default: 8, higher=better)

Default: `8`

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

