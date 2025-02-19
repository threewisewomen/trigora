# src/utils/config.py

TERRAIN_SETTINGS = {
    "width": 150,  # Default map width
    "height": 100,  # Default map height
    "scale": 50,  # Noise scale for Perlin noise
    "octaves": 6,  # Number of layers for noise
    "persistence": 0.5,  # Amplitude reduction per octave
    "lacunarity": 2.0,  # Frequency increase per octave
    "sea_level": -0.3,  # Noise threshold for water
    "mountain_level": 0.5,  # Noise threshold for mountains
    "forest_threshold": 0.1,  # Noise threshold for forests
    "smoothing_iterations": 5  # Number of smoothing passes
}

COLOR_MAP = {
    "W": (0.2, 0.5, 1.0),  # Water - Blue
    "M": (0.5, 0.5, 0.5),  # Mountain - Gray
    "F": (0.2, 0.7, 0.2),  # Forest - Green
    "P": (0.9, 0.8, 0.6),  # Plains - Tan
    "#": (0.2, 0.2, 0.2),  # Walls (for debugging)
    " ": (1.0, 1.0, 1.0)   # Empty space (for debugging)
}
