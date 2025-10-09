import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display


def plot_spectrogram(audio_path: str, sr: int = 22050, n_fft: int = 2048, hop_length: int = 512):
    """
    Визуализирует спектрограмму звукового файла.

    Args:
        audio_path (str): путь к аудиофайлу
        sr (int): частота дискретизации
        n_fft (int): размер окна для FFT
        hop_length (int): шаг окна
    """
    y, sr = librosa.load(audio_path, sr=sr)
    S = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    plt.figure(figsize=(10, 5))
    librosa.display.specshow(S_db, sr=sr, hop_length=hop_length, x_axis="time", y_axis="hz", cmap="magma")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python spectrogram_viewer.py <audio_file>")
    else:
        plot_spectrogram(sys.argv[1])
