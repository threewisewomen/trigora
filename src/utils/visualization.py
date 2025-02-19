import matplotlib.pyplot as plt
import numpy as np
from utils.config import COLOR_MAP


def plot_level(terrain_map, noise_map):
    """
    Plots the terrain map with gradient colors and contour lines.

    Parameters:
    - terrain_map: 2D numpy array of terrain characters ('W', 'P', 'M', 'F').
    - noise_map: 2D numpy array of Perlin noise values.

    Returns:
    - A Matplotlib figure for display.
    """

    height, width = terrain_map.shape
    rgb_values = np.zeros((height, width, 3))  # Initialize empty RGB map

    for y in range(height):
        for x in range(width):
            terrain_type = terrain_map[y, x]
            base_color = COLOR_MAP[terrain_type]

            # Adjust color brightness based on Perlin noise
            noise_value = noise_map[y, x]
            shade_factor = (noise_value + 1) / 2  # Normalize to (0,1)
            shaded_color = tuple(c * shade_factor for c in base_color)

            rgb_values[y, x, :] = shaded_color

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(rgb_values, interpolation='nearest')

    # Add contour lines
    contour_levels = 10
    contour_colors = 'k'
    X, Y = np.meshgrid(np.arange(width), np.arange(height))
    ax.contour(X, Y, noise_map, levels=contour_levels, colors=contour_colors, linewidths=0.5)

    # Hide axis ticks
    plt.xticks([])
    plt.yticks([])

    return fig
