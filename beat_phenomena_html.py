"""
Beat Phenomena Simulation - HTML Interactive Version
Demonstrates the interference pattern created by two waves with slightly different frequencies.
Renders visualization in HTML using Plotly for interactive exploration.
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Parameters
A = 1           # Amplitude
f1 = 260        # Frequency 1 (Hz)
f2 = 252        # Frequency 2 (Hz)

# Derived parameters
f_beat = abs(f1 - f2)  # Beat frequency
f_avg = (f1 + f2) / 2   # Average frequency

# Time array (2 seconds to show multiple beats)
duration = 2  # seconds
sampling_rate = 10000  # samples per second
t = np.linspace(0, duration, int(duration * sampling_rate))

# Individual waves
wave1 = A * np.sin(2 * np.pi * f1 * t)
wave2 = A * np.sin(2 * np.pi * f2 * t)

# Resultant wave (superposition)
resultant = wave1 + wave2

# Envelope (amplitude modulation)
envelope_upper = 2 * A * np.abs(np.cos(2 * np.pi * f_beat * t / 2))
envelope_lower = -envelope_upper

# Print information
print("=" * 60)
print("BEAT PHENOMENA SIMULATION")
print("=" * 60)
print(f"Amplitude (A):           {A}")
print(f"Frequency 1 (f1):        {f1} Hz")
print(f"Frequency 2 (f2):        {f2} Hz")
print(f"Beat Frequency (f_beat): {f_beat} Hz")
print(f"Average Frequency:       {f_avg} Hz")
print(f"Beat Period:             {1/f_beat:.3f} s")
print("=" * 60)
print("\nThe beat frequency is the difference between the two frequencies.")
print(f"You should hear {f_beat} beats per second.")
print("=" * 60)

# Create subplots
fig = make_subplots(
    rows=4, cols=1,
    subplot_titles=(
        f'Wave 1 (f1 = {f1} Hz)',
        f'Wave 2 (f2 = {f2} Hz)',
        'Resultant Wave (Beat Pattern) - Zoomed',
        f'Complete Beat Pattern (Beat Frequency = {f_beat} Hz)'
    ),
    vertical_spacing=0.08
)

# Plot 1: First wave (zoomed to 0.2 seconds)
fig.add_trace(
    go.Scatter(x=t[t <= 0.2], y=wave1[t <= 0.2], 
               mode='lines', name=f'Wave 1: f1 = {f1} Hz',
               line=dict(color='blue', width=1)),
    row=1, col=1
)

# Plot 2: Second wave (zoomed to 0.2 seconds)
fig.add_trace(
    go.Scatter(x=t[t <= 0.2], y=wave2[t <= 0.2], 
               mode='lines', name=f'Wave 2: f2 = {f2} Hz',
               line=dict(color='red', width=1)),
    row=2, col=1
)

# Plot 3: Resultant wave with envelope (zoomed to 0.2 seconds)
mask_zoom = t <= 0.2
fig.add_trace(
    go.Scatter(x=t[mask_zoom], y=resultant[mask_zoom], 
               mode='lines', name='Resultant Wave',
               line=dict(color='green', width=1)),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=t[mask_zoom], y=envelope_upper[mask_zoom], 
               mode='lines', name='Envelope',
               line=dict(color='black', width=2, dash='dash')),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=t[mask_zoom], y=envelope_lower[mask_zoom], 
               mode='lines', name='Envelope (lower)',
               line=dict(color='black', width=2, dash='dash'),
               showlegend=False),
    row=3, col=1
)

# Plot 4: Full duration showing multiple beats
fig.add_trace(
    go.Scatter(x=t, y=resultant, 
               mode='lines', name='Resultant Wave (Full)',
               line=dict(color='green', width=1)),
    row=4, col=1
)
fig.add_trace(
    go.Scatter(x=t, y=envelope_upper, 
               mode='lines', name='Envelope (Full)',
               line=dict(color='black', width=2, dash='dash')),
    row=4, col=1
)
fig.add_trace(
    go.Scatter(x=t, y=envelope_lower, 
               mode='lines', name='Envelope (lower, Full)',
               line=dict(color='black', width=2, dash='dash'),
               showlegend=False),
    row=4, col=1
)

# Update axes labels
fig.update_xaxes(title_text="Time (s)", row=4, col=1)
fig.update_yaxes(title_text="Amplitude", row=1, col=1)
fig.update_yaxes(title_text="Amplitude", row=2, col=1)
fig.update_yaxes(title_text="Amplitude", row=3, col=1)
fig.update_yaxes(title_text="Amplitude", row=4, col=1)

# Update layout
fig.update_layout(
    height=1200,
    title_text="Beat Phenomena Simulation - Interactive Visualization",
    showlegend=True,
    hovermode='x unified'
)

# Save to HTML file
output_file = 'beat_phenomena_interactive.html'
fig.write_html(output_file)

print(f"\n[SUCCESS] Interactive HTML visualization saved to: {output_file}")
print("[INFO] Open this file in your web browser to explore the beat phenomena.")
print("[INFO] You can zoom, pan, and hover over the plots for detailed values.")
print("=" * 60)
