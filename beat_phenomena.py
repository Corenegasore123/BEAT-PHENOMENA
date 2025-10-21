"""
Beat Phenomena Simulation
Demonstrates the interference pattern created by two waves with slightly different frequencies.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid rendering issues
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

# Create figure with subplots
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
fig.suptitle('Beat Phenomena Simulation', fontsize=16, fontweight='bold')

# Plot 1: First wave
axes[0].plot(t, wave1, 'b-', linewidth=0.5, label=f'Wave 1: f₁ = {f1} Hz')
axes[0].set_ylabel('Amplitude')
axes[0].set_title(f'Wave 1 (f₁ = {f1} Hz)')
axes[0].grid(True, alpha=0.3)
axes[0].legend()
axes[0].set_xlim(0, 0.2)  # Show first 0.2 seconds for clarity

# Plot 2: Second wave
axes[1].plot(t, wave2, 'r-', linewidth=0.5, label=f'Wave 2: f₂ = {f2} Hz')
axes[1].set_ylabel('Amplitude')
axes[1].set_title(f'Wave 2 (f₂ = {f2} Hz)')
axes[1].grid(True, alpha=0.3)
axes[1].legend()
axes[1].set_xlim(0, 0.2)

# Plot 3: Resultant wave with envelope
axes[2].plot(t, resultant, 'g-', linewidth=0.5, label='Resultant Wave')
axes[2].plot(t, envelope_upper, 'k--', linewidth=1.5, label='Envelope', alpha=0.7)
axes[2].plot(t, envelope_lower, 'k--', linewidth=1.5, alpha=0.7)
axes[2].set_ylabel('Amplitude')
axes[2].set_title(f'Resultant Wave (Beat Pattern)')
axes[2].grid(True, alpha=0.3)
axes[2].legend()
axes[2].set_xlim(0, 0.2)

# Plot 4: Full duration showing multiple beats
axes[3].plot(t, resultant, 'g-', linewidth=0.5, label='Resultant Wave')
axes[3].plot(t, envelope_upper, 'k--', linewidth=1.5, label='Envelope', alpha=0.7)
axes[3].plot(t, envelope_lower, 'k--', linewidth=1.5, alpha=0.7)
axes[3].set_xlabel('Time (s)')
axes[3].set_ylabel('Amplitude')
axes[3].set_title(f'Complete Beat Pattern (Beat Frequency = {f_beat} Hz)')
axes[3].grid(True, alpha=0.3)
axes[3].legend()

plt.tight_layout()

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

# Save the plot to a file
output_file = 'beat_phenomena_plot.png'
plt.savefig(output_file, dpi=150, bbox_inches='tight')
print(f"\nPlot saved to: {output_file}")
print("You can view the visualization in the saved image file.")

# Uncomment the line below to display the plot interactively
# plt.show()

# Optional: Create an animation showing how beats form
def create_animation():
    """Create an animated visualization of beat formation"""
    fig_anim, ax = plt.subplots(figsize=(12, 6))
    
    # Time window for animation
    t_window = np.linspace(0, 0.5, 1000)
    
    line1, = ax.plot([], [], 'b-', linewidth=1, alpha=0.5, label=f'f₁ = {f1} Hz')
    line2, = ax.plot([], [], 'r-', linewidth=1, alpha=0.5, label=f'f₂ = {f2} Hz')
    line_result, = ax.plot([], [], 'g-', linewidth=2, label='Resultant')
    
    ax.set_xlim(0, 0.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Beat Phenomena - Real-time Formation')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        line_result.set_data([], [])
        return line1, line2, line_result
    
    def animate(frame):
        t_current = t_window[:frame*10]
        if len(t_current) > 0:
            y1 = A * np.sin(2 * np.pi * f1 * t_current)
            y2 = A * np.sin(2 * np.pi * f2 * t_current)
            y_result = y1 + y2
            
            line1.set_data(t_current, y1)
            line2.set_data(t_current, y2)
            line_result.set_data(t_current, y_result)
        
        return line1, line2, line_result
    
    anim = FuncAnimation(fig_anim, animate, init_func=init, 
                        frames=100, interval=50, blit=True)
    plt.show()

# Uncomment to run animation
# create_animation()
