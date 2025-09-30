# Servicio de detección de sonidos
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav

def detect_can_opening(audio_chunk):
    # Aquí podrías cargar un modelo preentrenado o hacer un análisis de espectro
    # Ejemplo placeholder:
    if np.mean(audio_chunk) > 0.5:  # Umbral ficticio
        return True
    return False
