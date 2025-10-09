import numpy as np
import sounddevice as sd
import scipy.signal as signal

# Duración en segundos que se analiza
DURATION = 2  
SAMPLE_RATE = 44100  

def listen_for_sounds():
    print("🎧 Escuchando sonidos...")
    recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()

    # Transformada rápida de Fourier (espectro de frecuencias)
    freqs, times, Sxx = signal.spectrogram(recording[:, 0], SAMPLE_RATE)

    # Heurística simple: detectar un "pico" rápido de energía
    energy = np.sum(Sxx, axis=0)  
    peak = np.max(energy)

    # Ajusta el umbral probando con grabaciones reales
    if peak > 1e-3:  
        print("🥤 ¡Sonido detectado! (posible lata)")
        return "can_opening"
    else:
        return None
