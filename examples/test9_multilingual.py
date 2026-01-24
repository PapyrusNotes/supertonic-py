"""
Example 9: Multilingual Synthesis

Demonstrates Supertonic-2's multilingual support.
Supported languages: English (en), Korean (ko), Spanish (es), Portuguese (pt), French (fr)
"""

import os

from supertonic import TTS

os.makedirs("outputs/test9", exist_ok=True)

tts = TTS()
style = tts.get_voice_style("M1")

# Multilingual examples
examples = [
    ("en", "Welcome to Supertonic! This is an English text-to-speech synthesis."),
    ("ko", "안녕하세요! 수퍼토닉에 오신 것을 환영합니다. 한국어 음성 합성입니다."),
    ("es", "¡Bienvenido a Supertonic! Esta es una síntesis de voz en español."),
    ("pt", "Bem-vindo ao Supertonic! Esta é uma síntese de voz em português."),
    ("fr", "Bienvenue sur Supertonic! Ceci est une synthèse vocale en français."),
]

print("🌐 Multilingual TTS Examples\n")
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

