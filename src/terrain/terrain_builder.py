import numpy as np

def apply_terrain_features(noise_map, sea_level, mountain_level, forest_threshold):
    """
    Converts a Perlin noise map into terrain features.

    Parameters:
    - noise_map: 2D numpy array of noise values.
    - sea_level: Threshold for water.
    - mountain_level: Threshold for mountains.
    - forest_threshold: Threshold for forested areas.

    Returns:
    - 2D array of terrain characters ('W', 'P', 'M', 'F').
    """

    height, width = noise_map.shape
    terrain_map = np.full((height, width), 'P')  # Default to Plains ('P')

    for y in range(height):
        for x in range(width):
            noise_value = noise_map[y, x]

            if noise_value < sea_level:
                terrain_map[y, x] = 'W'  # Water
            elif noise_value < mountain_level:
                if noise_value > forest_threshold:
                    terrain_map[y, x] = 'F'  # Forest
                else:
                    terrain_map[y, x] = 'P'  # Plains
            else:
                terrain_map[y, x] = 'M'  # Mountain

    return terrain_map
