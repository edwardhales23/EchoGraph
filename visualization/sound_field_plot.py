import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_sound_field(positions: np.ndarray, intensities: np.ndarray, cmap: str = "plasma"):
    """
    Визуализирует звуковое поле в 3D пространстве.

    Args:
        positions (np.ndarray): координаты микрофонов или источников звука (N x 3)
        intensities (np.ndarray): значения интенсивности звука для каждой точки (N,)
        cmap (str): цветовая карта для отображения интенсивностей
    """
    if positions.shape[1] != 3:
        raise ValueError("positions must have shape (N, 3)")

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    p = ax.scatter(
        positions[:, 0], positions[:, 1], positions[:, 2],
        c=intensities, cmap=cmap, s=50, alpha=0.8
    )

    plt.colorbar(p, ax=ax, label="Sound Intensity (dB)")
    ax.set_xlabel("X axis (m)")
    ax.set_ylabel("Y axis (m)")
    ax.set_zlabel("Z axis (m)")
    ax.set_title("3D Sound Field Visualization")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Пример с синтетическими данными
    N = 100
    positions = np.random.rand(N, 3) * 10
    intensities = np.sin(positions[:, 0])**2 + np.cos(positions[:, 1])**2
    plot_sound_field(positions, intensities)
