from services.recognizer import listen_and_recognize
from services.player import play_audio
from commands.command_handler import handle_command

def main():
    print("🎤 Asistente de gimnasio iniciado. Escuchando...")
    while True:
        text = listen_and_recognize()
        if text:
            print(f"Reconocido: {text}")
            handle_command(text.lower())

if __name__ == "__main__":
    main()
