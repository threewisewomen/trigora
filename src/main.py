import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from terrain import generate_noise_map, apply_terrain_features, smooth_terrain
from utils.visualization import plot_level
from utils.config import TERRAIN_SETTINGS


def main():
    """Main function to run the Streamlit fantasy map generator."""
    st.title("Trigora Fantasy Map Generator 🗺️")
    st.caption("Adjust the parameters in the sidebar and generate a new fantasy map!")

    # Sidebar for user input
    st.sidebar.header("Map Parameters")
    
    width = st.sidebar.slider("Width", 50, 250, TERRAIN_SETTINGS["width"])
    height = st.sidebar.slider("Height", 50, 200, TERRAIN_SETTINGS["height"])
    scale = st.sidebar.slider("Noise Scale", 10, 100, TERRAIN_SETTINGS["scale"])
    octaves = st.sidebar.slider("Noise Octaves", 1, 10, TERRAIN_SETTINGS["octaves"])
    persistence = st.sidebar.slider("Noise Persistence", 0.1, 1.0, TERRAIN_SETTINGS["persistence"])
    lacunarity = st.sidebar.slider("Noise Lacunarity", 1.0, 4.0, TERRAIN_SETTINGS["lacunarity"])
    sea_level = st.sidebar.slider("Sea Level", -1.0, 0.0, TERRAIN_SETTINGS["sea_level"])
    mountain_level = st.sidebar.slider("Mountain Level", 0.0, 1.0, TERRAIN_SETTINGS["mountain_level"])
    forest_threshold = st.sidebar.slider("Forest Threshold", -0.5, 0.5, TERRAIN_SETTINGS["forest_threshold"])
    smoothing_iterations = st.sidebar.slider("Smoothing Iterations", 0, 10, TERRAIN_SETTINGS["smoothing_iterations"])

    # Generate noise map
    noise_map = generate_noise_map(width, height, scale, octaves, persistence, lacunarity)

    # Apply terrain features
    level = apply_terrain_features(noise_map, sea_level, mountain_level, forest_threshold)

    # Smooth terrain
    level = smooth_terrain(level, smoothing_iterations)

    # Plot and display the generated terrain
    fig = plot_level(level, noise_map)
    st.pyplot(fig)

    # Button to regenerate the map
    if st.button("Generate New Map 🔄"):
        st.experimental_rerun()


if __name__ == "__main__":
    main()
