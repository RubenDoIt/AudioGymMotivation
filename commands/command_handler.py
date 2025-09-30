# Lógica para detectar y ejecutar comandos
from services.player import play_audio
from commands.voice_commands import VOICE_COMMANDS

def handle_command(text: str):
    for key, action in VOICE_COMMANDS.items():
        if key in text:
            play_audio(action)
            return
    print("⚠️ Comando no reconocido")
