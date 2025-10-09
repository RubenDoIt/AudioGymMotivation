from services.recognizer import listen_and_recognize
from services.sound_detector import listen_for_sounds
from commands.command_handler import handle_command, handle_sound

def main():
    print("🎤 Asistente de gimnasio iniciado. Escuchando...")
    while True:
        # 1. Voz
        text = listen_and_recognize()
        if text:
            print(f"Reconocido: {text}")
            handle_command(text.lower())

        # 2. Sonidos (ejemplo cada ciclo analiza 2s de audio)
        sound_event = listen_for_sounds()
        if sound_event:
            print(f"Reproducioendo: {sound_event}")
            handle_sound(sound_event)

if __name__ == "__main__":
    main()
