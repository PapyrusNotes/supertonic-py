#### `--host`

Interface to bind (default: 127.0.0.1; loopback only)

Default: `127.0.0.1`

#### `--port`

Port to listen on (default: 7788)

Default: `7788`

#### `--model`

Possible choices: `supertonic`, `supertonic-2`, `supertonic-3`

Model to load on startup (default: supertonic-3)

Default: `supertonic-3`

#### `--cors`

Comma-separated CORS origins to allow (e.g. 'http://localhost:*,chrome-extension://*'). Omit to disable CORS entirely.

#### `--log-level`

Possible choices: `critical`, `error`, `warning`, `info`, `debug`, `trace`

uvicorn log level (default: info)

Default: `info`

#### `-v`, `--verbose`

Enable verbose output with detailed logging

Default: `False`

