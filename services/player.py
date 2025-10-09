# Servicio de reproducción de audio
import pygame
import os

pygame.mixer.init()

def play_audio(file_path: str):
    try:
        audio_name = os.path.basename(file_path)
        print(f"Reproduciendo: {audio_name}")
        
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Error al reproducir {file_path}: {e}")
