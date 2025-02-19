import numpy as np

def smooth_terrain(terrain_map, iterations=1):
    """
    Smooths the terrain by checking neighboring tiles and adjusting terrain types.

    Parameters:
    - terrain_map: 2D numpy array of terrain characters ('W', 'P', 'M', 'F').
    - iterations: Number of smoothing passes.

    Returns:
    - A refined 2D numpy array of terrain characters.
    """

    height, width = terrain_map.shape

    for _ in range(iterations):
        new_map = terrain_map.copy()

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                neighbors = [
                    terrain_map[y - 1, x - 1], terrain_map[y - 1, x], terrain_map[y - 1, x + 1],
                    terrain_map[y, x - 1], terrain_map[y, x + 1],
                    terrain_map[y + 1, x - 1], terrain_map[y + 1, x], terrain_map[y + 1, x + 1]
                ]

                current_type = terrain_map[y, x]

                # Rule: If more than half the neighbors are a different type, change it
                if neighbors.count('M') > 4:
                    new_map[y, x] = 'M'
                elif neighbors.count('F') > 5:
                    new_map[y, x] = 'F'
                elif neighbors.count('W') > 4:
                    new_map[y, x] = 'W'
                else:
                    new_map[y, x] = 'P'

        terrain_map = new_map  # Update terrain map after each iteration

    return terrain_map
