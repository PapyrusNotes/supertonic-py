# Security Policy

## Reporting a Vulnerability

If you discover a security issue in **supertonic-py** — including in the
package itself, the model loader, the CLI, or in the way the package
fetches model weights from Hugging Face Hub — please report it
privately rather than opening a public GitHub issue or pull request.

**Contact:** [contact@supertone.ai](mailto:contact@supertone.ai)

Please include:

- A short description of the issue and the impact you observed
- Steps to reproduce (a minimal code sample is ideal)
- The `supertonic` version (`python -c "import supertonic; print(supertonic.__version__)"`),
  Python version, and OS
- Whether the issue requires a specific Hugging Face Hub revision or
  custom voice-style JSON to reproduce
- Any suggested mitigation, if you have one

We aim to acknowledge new reports within **5 business days**, follow up
with a triage decision within **10 business days**, and coordinate a
fix and a coordinated disclosure timeline from there. If you do not
hear back within those windows, feel free to nudge the same address.

## Supported Versions

Security fixes are made to the latest minor release line. Older minor
versions only receive fixes for issues judged Critical at our discretion.

| Version  | Supported          |
|----------|--------------------|
| 1.2.x    | :white_check_mark: |
| 1.1.x    | :warning: Critical fixes only |
| 1.0.x    | :x: End of life     |
| < 1.0    | :x: End of life     |

## Scope

In scope for security reports:

- Arbitrary code execution, path traversal, or unsafe deserialization in
  the model loader, voice-style loader (`get_voice_style_from_path`), or
  CLI argument parsing
- Tampering with the model download (e.g. cache poisoning, TOFU issues
  when the pinned Hugging Face Hub revision is overridden)
- Unintended exposure of secrets or local files via the CLI or library
  APIs
- Supply-chain issues in our build / publish pipeline
  (`.github/workflows/publish.yml`)

Out of scope (please report these via normal GitHub issues instead):

- Bugs that only affect synthesis quality
- Feature requests
- Model behavior / hallucinations / synthesis quality on adversarial
  text inputs (these are usability and model-quality concerns rather
  than software vulnerabilities — see the model card for limitations)
- Issues that require physical access to the user's machine or root /
  administrator privileges on it

## Related Resources

- Model license: [OpenRAIL-M](https://huggingface.co/Supertone/supertonic-3/blob/main/LICENSE)
- Package license: [MIT](LICENSE)
- Responsible-use guidance for voice cloning will be added to the
  documentation site (`docs/responsible-use.md`) in a follow-up release.
