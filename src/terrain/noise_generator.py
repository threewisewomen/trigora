import noise
import random
import numpy as np


def generate_noise_map(width, height, scale, octaves, persistence, lacunarity):
    """
    Generates a 2D Perlin noise map.

    Parameters:
    - width, height: Dimensions of the map.
    - scale: Controls the frequency of the noise.
    - octaves: Number of layers of noise.
    - persistence: Amplitude reduction per octave.
    - lacunarity: Frequency increase per octave.

    Returns:
    - A 2D numpy array representing the noise map.
    """
    if scale <= 0:
        raise ValueError("Scale must be greater than 0")

    offset_x = random.uniform(0, 10000)  # Random offsets to avoid repetitive patterns
    offset_y = random.uniform(0, 10000)

    noise_map = np.zeros((height, width))  # Initialize empty noise map

    for y in range(height):
        for x in range(width):
            noise_map[y, x] = noise.pnoise2(
                (x / scale) + offset_x,
                (y / scale) + offset_y,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=width,
                repeaty=height,
                base=0
            )

    return noise_map
