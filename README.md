# Beat Phenomena Simulator

Interactive web-based simulation and visualization of beat phenomena that occurs when two sound waves with slightly different frequencies interfere with each other.

## Two Versions Available

### 1. JavaScript Interactive Version (`beat_simulator.html`)
- **No installation required** - Runs directly in your browser
- **Real-time parameter control** - Adjust amplitude and frequencies on the fly
- **Instant updates** - Generate new simulations with different parameters
- **Pure client-side** - No Python or server needed

### 2. Python Generated Version (`generate_plots.py`)
- **Python-powered calculations** - Uses NumPy for precise wave calculations
- **Plotly visualization** - Professional interactive plots
- **Customizable** - Modify the script to change default parameters
- **Generates static HTML** - Creates `beat_simulation_python.html`

## Features

- **Professional Visualization** - Four synchronized subplots showing wave interference
- **Full Plotly Interactivity** - Zoom, pan, box select, scroll zoom, and more
- **Responsive Design** - Works on desktop and mobile devices
- **Clean Professional UI** - Modern design with Font Awesome icons

## Default Parameters
- **Amplitude (A)**: 1
- **Frequency 1 (f₁)**: 260 Hz
- **Frequency 2 (f₂)**: 252 Hz
- **Beat Frequency**: 8 Hz (|f₁ - f₂|)

## Physics Background

When two waves of slightly different frequencies are superimposed, they produce a phenomenon called **beats**. The resultant wave has:
- A frequency equal to the average of the two frequencies: (f₁ + f₂) / 2
- An amplitude that varies periodically at the beat frequency: |f₁ - f₂|

The mathematical representation:
```
y₁(t) = A sin(2πf₁t)
y₂(t) = A sin(2πf₂t)
y_resultant(t) = y₁(t) + y₂(t) = 2A cos(2πf_beat·t/2) sin(2πf_avg·t)
```

## Usage

Simply open `beat_simulator.html` in any modern web browser:

```bash
# Windows
start beat_simulator.html

# macOS
open beat_simulator.html

# Linux
xdg-open beat_simulator.html
```

Or double-click the file in your file explorer.

## Interactive Features

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

## Output

The simulation calculates and displays:
- **Beat Frequency**: |f₁ - f₂| Hz
- **Average Frequency**: (f₁ + f₂) / 2 Hz
- **Beat Period**: 1 / f_beat seconds
- **Amplitude Envelope**: Shows the "beating" effect pattern

## Technical Details

- **Technology**: Pure HTML/CSS/JavaScript with Plotly.js
- **No Dependencies**: All libraries loaded from CDN
- **Offline Capable**: Can be saved and used without internet (after first load)
- **Browser Support**: Chrome, Firefox, Safari, Edge (modern versions)
