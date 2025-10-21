<div align="center">

# 🌊 Beat Phenomena Simulator

### Interactive Physics Visualization Tool

[![Made with Plotly](https://img.shields.io/badge/Made%20with-Plotly-3F4F75.svg)](https://plotly.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)

**A professional, interactive web-based simulation and visualization of beat phenomena**

Explore what happens when two sound waves with slightly different frequencies interfere with each other!

</div>

---

## 📋 Table of Contents

- [Three Versions Available](#-three-versions-available)
- [Features](#-features)
- [Physics Background](#-physics-background)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Interactive Features](#-interactive-features)
- [Dependencies](#-dependencies)
- [Contributing](#-contributing)
- [Notes](#-notes)
- [Support](#-support)

---

## 🎯 Three Versions Available

Choose the version that best fits your needs:

### Option 1: Plotly.js Only (JavaScript) ⚡
**File:** `beat_simulator.html`

✅ **Advantages:**
- ✨ **Zero installation** - Just open in your browser
- 🎮 **Real-time interactive controls** - Adjust parameters on the fly
- ⚡ **Instant updates** - Generate new simulations immediately
- 🌐 **Pure client-side** - No Python, no server, no setup
- 📱 **Works offline** - After first load, no internet needed

**Perfect for:** Quick demonstrations, teaching, presentations, or when you don't have Python installed

### Option 2: Python + Plotly 🐍
**File:** `generate_plots.py`

✅ **Advantages:**
- 🔬 **Scientific precision** - NumPy-powered calculations
- 🎨 **Customizable** - Modify code to add features or change defaults
- 📊 **Reproducible** - Generate consistent outputs for reports
- 💾 **Scriptable** - Integrate into larger workflows
- 📈 **Batch processing** - Generate multiple simulations programmatically
- 🌐 **Interactive HTML output** - Generates `beat_simulation_python.html`

**Perfect for:** Research, academic papers, custom analysis, or when you need Python's scientific computing power

### Option 3: Pure Python (Matplotlib) 📊
**File:** `beat_phenomena.py`

✅ **Advantages:**
- 📈 **Classic matplotlib** - Traditional scientific plotting
- 🖥️ **Desktop application** - Native window display
- 🔧 **Lightweight** - No web dependencies
- 📝 **Educational** - Great for learning Python plotting
- 💻 **Offline** - Completely standalone Python script

**Perfect for:** Traditional Python workflows, offline analysis, or when you prefer matplotlib over web-based plots

## ✨ Features

### Visualization
- 📊 **Four synchronized subplots** showing complete wave interference analysis
- 🎯 **Professional design** with clean, modern UI and Font Awesome icons
- 📱 **Fully responsive** - Works seamlessly on desktop, tablet, and mobile
- 🎨 **Color-coded waves** - Easy to distinguish between components

### Interactivity (Plotly.js)
- 🔍 **Scroll zoom** - Use mouse wheel to zoom in/out on any subplot
- 📦 **Box select** - Click and drag to zoom into specific regions
- 🖱️ **Pan mode** - Navigate around the plots freely
- 💾 **Export** - Download high-quality PNG images (1400x1200, 2x scale)
- 🔄 **Reset view** - Double-click to restore original zoom
- 📍 **Hover tooltips** - See exact values at any point
- 🎛️ **Live controls** - Adjust amplitude and frequencies in real-time

### Calculations
- 🧮 **Accurate physics** - Proper wave superposition and beat frequency
- 📐 **Envelope visualization** - Shows amplitude modulation clearly
- 📊 **Results panel** - Displays all calculated parameters
- ⏱️ **Beat period** - Automatically calculated and displayed

## 🔢 Default Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| **Amplitude (A)** | 1 | Wave amplitude |
| **Frequency 1 (f₁)** | 260 Hz | First wave frequency |
| **Frequency 2 (f₂)** | 252 Hz | Second wave frequency |
| **Beat Frequency** | 8 Hz | |f₁ - f₂| |
| **Average Frequency** | 256 Hz | (f₁ + f₂) / 2 |
| **Beat Period** | 0.125 s | 1 / f_beat |

## 🔬 Physics Background

When two waves of slightly different frequencies are superimposed, they produce a phenomenon called **beats**. The resultant wave has:
- A frequency equal to the average of the two frequencies: (f₁ + f₂) / 2
- An amplitude that varies periodically at the beat frequency: |f₁ - f₂|

The mathematical representation:
```
y₁(t) = A sin(2πf₁t)
y₂(t) = A sin(2πf₂t)
y_resultant(t) = y₁(t) + y₂(t) = 2A cos(2πf_beat·t/2) sin(2πf_avg·t)
```

## 🚀 Quick Start

### Method 1: JavaScript Version (Recommended for Quick Use)

1. **Download** or clone this repository
2. **Open** `beat_simulator.html` in any modern web browser
   - Windows: Double-click or `start beat_simulator.html`
   - macOS: Double-click or `open beat_simulator.html`
   - Linux: Double-click or `xdg-open beat_simulator.html`
3. **Adjust** parameters using the input fields
4. **Click** "Generate Simulation" to update the plots

That's it! No installation needed.

### Method 2: Python + Plotly Version

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python generate_plots.py
   ```

3. **Open** the generated `beat_simulation_python.html` file

### Method 3: Pure Python (Matplotlib) Version

1. **Install dependencies:**
   ```bash
   pip install numpy matplotlib
   ```

2. **Run the script:**
   ```bash
   python beat_phenomena.py
   ```

3. **View** the plots in the matplotlib window that opens

## 📖 Usage

## 🎮 Interactive Features

### Input Controls
- Adjust **Amplitude (A)** from 0.1 to 10
- Set **Frequency 1 (f₁)** from 1 to 1000 Hz
- Set **Frequency 2 (f₂)** from 1 to 1000 Hz
- Click **Generate Simulation** to update plots
- Click **Reset Defaults** to restore original values

### Visualization
The simulator displays four synchronized plots:
1. **Wave 1** - First frequency component (zoomed to 0.2s)
2. **Wave 2** - Second frequency component (zoomed to 0.2s)
3. **Resultant Wave with Envelope** - Beat pattern detail (zoomed to 0.2s)
4. **Complete Beat Pattern** - Full 2-second view showing multiple beats

### Plotly Tools
- **Scroll Zoom** - Use mouse wheel to zoom in/out
- **Box Zoom** - Click and drag to select zoom area
- **Pan** - Move around the plot
- **Download** - Export as high-quality PNG
- **Reset** - Double-click to reset view
- **Hover** - See exact values at any point

## 📊 Output

The simulation calculates and displays:
- **Beat Frequency**: |f₁ - f₂| Hz
- **Average Frequency**: (f₁ + f₂) / 2 Hz
- **Beat Period**: 1 / f_beat seconds
- **Amplitude Envelope**: Shows the "beating" effect pattern

## 🛠️ Dependencies

### JavaScript Version
- **Plotly.js** (loaded from CDN) - Interactive plotting library
- **Font Awesome** (loaded from CDN) - Icons
- **Google Fonts** (loaded from CDN) - Inter font family

**No installation required!** All dependencies are loaded automatically from CDN.

### Python Version
- **Python 3.7+**
- **NumPy** >= 1.21.0 - Numerical computing
- **Plotly** >= 5.0.0 - Interactive plotting

Install with: `pip install -r requirements.txt`

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

### How to Contribute

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 💡 Technical Details

### JavaScript Version
- **Technology Stack**: Pure HTML5, CSS3, JavaScript (ES6+)
- **Libraries**: Plotly.js, Font Awesome, Google Fonts
- **Architecture**: Single-page application, no build process
- **File Size**: ~30 KB (excluding CDN libraries)
- **Browser Support**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

### Python Version  
- **Technology Stack**: Python 3, NumPy, Plotly
- **Output**: Static HTML with embedded JavaScript
- **File Size**: Generated HTML ~8 KB + embedded plot data
- **Customization**: Easily modify parameters in the script

## ⭐ Support

### Found this helpful?

If you find this project useful, please consider:

- ⭐ **Starring the repository** - It helps others discover this tool!
- 🤝 **Contributing** - Submit pull requests with improvements

---

<div align="center">

**Made with ❤️ for physics education and visualization**

If this project helped you, please ⭐ star the repository!

</div>
