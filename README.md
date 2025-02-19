# **Trigora Fantasy Map Generator** 🗺️  

**A procedurally generated fantasy map creator using Perlin noise and Streamlit.**  

## **📌 Features**  
✅ **Interactive UI** – Adjust map parameters in real time  
✅ **Procedural Generation** – Unique terrain every time  
✅ **Perlin Noise-Based Terrain** – Realistic landforms  
✅ **Dynamic Visualization** – Color-coded maps with contour lines  
✅ **Regeneration Button** – Instantly create new maps  

---

## **🚀 How It Works**  

### **1️⃣ `main.py` (Entry Point)**
🔹 **Handles the user interface with Streamlit**  
🔹 **Takes user input from sidebar controls**  
🔹 **Generates a terrain using procedural techniques**  
🔹 **Displays the generated map using Matplotlib**  

### **🖥️ UI Overview**  
- `st.title()` → Displays the app title  
- `st.sidebar.slider()` → Adjust map parameters dynamically  
- `"Generate New Map"` → Regenerates a new random map  

---

## **🔧 Modules Overview**  

### **📝 `config.py` (Configuration File)**  
Stores global constants for easier modifications.  

- **`TERRAIN_SETTINGS`** → Default parameters for terrain generation  
- **`COLOR_MAP`** → Defines RGB colors for different terrain types  

---

### **📝 `noise_generator.py` (Generating Perlin Noise)**  
🔹 Uses **Perlin noise (`noise.pnoise2`)** for smooth, natural-looking terrain.  
🔹 Avoids repetitive patterns using **random offsets**.  
🔹 Returns a **2D NumPy array** where values represent terrain elevation.  

**Key Parameters:**  
✅ `scale` – Controls noise frequency (zoom level)  
✅ `octaves` – Number of noise layers (adds detail)  
✅ `persistence` – Controls fading details in higher octaves  
✅ `lacunarity` – Controls spacing between noise features  

---

### **📝 `terrain_builder.py` (Mapping Noise to Terrain Features)**  
Transforms **Perlin noise values** into **terrain types**:  

🌊 **Water (`W`)** – Below sea level  
🏞️ **Plains (`P`)** – Default land terrain  
🌲 **Forest (`F`)** – Mid-elevation zones  
⛰️ **Mountains (`M`)** – High-elevation zones  

🔹 Uses **NumPy for efficiency** and ensures every point is categorized.  

---

### **📝 `terrain_smoother.py` (Refining Terrain Features)**  
Improves **map realism** by adjusting terrain types based on **neighboring tiles**.  

**🛠️ Smoothing Rules:**  
✅ If **4+ neighbors are Water**, convert to Water (`W`).  
✅ If **5+ neighbors are Forest**, convert to Forest (`F`).  
✅ If **4+ neighbors are Mountains**, convert to Mountain (`M`).  
✅ Otherwise, remain as **Plains (`P`)**.  

🔹 **Runs multiple iterations** for natural-looking terrain transitions.  

---

### **📝 `visualization.py` (Rendering the Map)**  
Generates **color-coded, shaded terrain maps** using **Matplotlib**.  

🔹 **Uses `COLOR_MAP` for terrain shading**  
🔹 **Brighter = Higher elevation, Darker = Lower elevation**  
🔹 **Contour lines** help visualize altitude differences  

🖼️ **Displays the final map using `st.pyplot(fig)`** in the Streamlit UI.  

---

## **▶️ Running the Project**  
1️⃣ **Activate Virtual Environment**  
```sh
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```
2️⃣ **Run Streamlit App**  
```sh
streamlit run src/main.py
```
3️⃣ **Adjust map parameters** in the sidebar  
4️⃣ **Click "Generate New Map"** to create a new terrain  

---

## **🎯 Future Improvements**  
✅ **Add villages, rivers, and roads**  
✅ **Generate named locations dynamically**  
✅ **Improve terrain transitions with noise blending**  

---

### **👨‍💻 Contributing**  
Feel free to fork and improve the project! Open an issue if you have suggestions. 🚀  

---

