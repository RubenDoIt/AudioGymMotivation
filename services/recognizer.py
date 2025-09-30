# Servicio de reconocimiento de voz
import speech_recognition as sr

def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("❌ Error en el servicio de reconocimiento.")
        return None
