# Beat Phenomena Simulation

This Python script simulates and visualizes the beat phenomena that occurs when two sound waves with slightly different frequencies interfere with each other.

## Parameters
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

## Installation

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### HTML Interactive Version (Recommended)
Run the HTML version for interactive visualization:
```bash
python beat_phenomena_html.py
```

This will:
1. Generate an interactive HTML file (`beat_phenomena_interactive.html`)
2. Display four interactive plots showing:
   - Individual wave 1 (260 Hz)
   - Individual wave 2 (252 Hz)
   - Resultant wave with envelope (zoomed view)
   - Complete beat pattern over 2 seconds
3. Print simulation parameters and beat frequency information
4. Open the HTML file in your default browser

The HTML visualization allows you to:
- Zoom in/out on any region
- Pan across the timeline
- Hover to see exact values
- Toggle individual traces on/off

### Matplotlib Version
Run the matplotlib version (saves to PNG):
```bash
python beat_phenomena.py
```

## Optional Animation

To see an animated visualization of how beats form in real-time, uncomment the last line in the script:
```python
create_animation()
```

## Output

The simulation shows:
- **Beat Frequency**: 8 Hz (you would hear 8 beats per second)
- **Beat Period**: 0.125 seconds
- **Envelope**: The amplitude modulation pattern that creates the "beating" effect
