from services.player import play_audio
from commands.voice_commands import VOICE_COMMANDS
from commands.sound_commands import SOUND_COMMANDS

def handle_command(text: str):
    # Para comandos de voz
    for key, action in VOICE_COMMANDS.items():
        if key in text:
            play_audio(action)
            return
    print("⚠️ Comando de voz no reconocido")

def handle_sound(event: str):
    if event in SOUND_COMMANDS:
        play_audio(SOUND_COMMANDS[event])
