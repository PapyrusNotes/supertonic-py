"""
Example 9: Multilingual Synthesis

Demonstrates Supertonic-3's multilingual support.

Supertonic-3 covers 31 languages (en, ko, ja, ar, bg, cs, da, de, el, es, et,
fi, fr, hi, hr, hu, id, it, lt, lv, nl, pl, pt, ro, ru, sk, sl, sv, tr, uk, vi)
plus a special 'na' fallback for text whose language is unknown or outside
this set.
"""

import os

from supertonic import TTS

os.makedirs("outputs/test9", exist_ok=True)

tts = TTS()
style = tts.get_voice_style("M1")

# A handful of representative languages — Supertonic-3 supports 31 in total.
examples = [
    ("en", "Welcome to Supertonic! This is an English text-to-speech synthesis."),
    ("ko", "안녕하세요! 수퍼토닉에 오신 것을 환영합니다. 한국어 음성 합성입니다."),
    ("ja", "こんにちは！スーパートニックへようこそ。日本語の音声合成です。"),
    ("es", "¡Bienvenido a Supertonic! Esta es una síntesis de voz en español."),
    ("pt", "Bem-vindo ao Supertonic! Esta é uma síntese de voz em português."),
    ("fr", "Bienvenue sur Supertonic! Ceci est une synthèse vocale en français."),
    ("de", "Willkommen bei Supertonic! Dies ist eine deutsche Sprachsynthese."),
    ("it", "Benvenuto su Supertonic! Questa è una sintesi vocale in italiano."),
    # 'na' falls back to the language-agnostic <na> token for unknown languages
    ("na", "This text uses the unknown-language fallback."),
]

print("🌐 Multilingual TTS Examples (Supertonic-3)\n")
print("=" * 60)

for lang, text in examples:
    wav, duration = tts.synthesize(text, voice_style=style, lang=lang)
    output_path = f"outputs/test9/multilingual_{lang}.wav"
    tts.save_audio(wav, output_path)
    print(f"[{lang.upper()}] {duration[0]:.2f}s → {output_path}")
    print(f"     Text: {text[:50]}{'...' if len(text) > 50 else ''}")
    print()

print("=" * 60)
print("✅ All multilingual examples generated successfully!")
