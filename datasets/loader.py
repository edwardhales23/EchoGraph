




































































import numpy as np
import soundfile as sf


def generate_tone(frequency=440, duration=2.0, sample_rate=22050, amplitude=0.3, file_name="tone.wav"):
    """
    Generates a sinusoidal signal for testing

    Args:
        frequency (float): частота в Гц
        duration (float): длительность в секундах
        sample_rate (int): частота дискретизации
        amplitude (float): амплитуда (0–1)
        file_name (str): имя файла для сохранения
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    sf.write(file_name, y, sample_rate)
    print(f"✅ Тон {frequency} Гц сохранён как {file_name}")


if __name__ == "__main__":
    generate_tone(440)
