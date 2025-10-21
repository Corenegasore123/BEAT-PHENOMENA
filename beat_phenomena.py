import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1
f1 = 260  # Hz
f2 = 252  # Hz
duration = 10  # seconds
sampling_rate = 10000  # samples per second

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration))

# Two waves with close frequencies
y1 = A * np.sin(2 * np.pi * f1 * t)
y2 = A * np.sin(2 * np.pi * f2 * t)

# Resultant wave (superposition)
y_resultant = y1 + y2

# Calculate beat frequency (Δf) and average frequency (fb)
delta_f = abs(f1 - f2)  # Beat frequency
f_avg = (f1 + f2) / 2   # Average frequency

print(f"Frequency 1 (f1): {f1} Hz")
print(f"Frequency 2 (f2): {f2} Hz")
print(f"Beat frequency (Δf): {delta_f} Hz")
print(f"Average frequency (fb): {f_avg:.2f} Hz")

# Theoretical beat pattern
# The resultant can be written as: y = 2A * cos(2π*(Δf/2)t) * sin(2π*f_avg*t)
beat_envelope = 2 * A * np.cos(2 * np.pi * (delta_f/2) * t)
carrier_wave = np.sin(2 * np.pi * f_avg * t)
theoretical_beat = beat_envelope * carrier_wave

# Plotting
plt.figure(figsize=(12, 10))

# Individual waves
plt.subplot(4, 1, 1)
plt.plot(t[:2000], y1[:2000], 'b-', linewidth=1)
plt.title(f'Wave 1: {f1} Hz')
plt.ylabel('Amplitude')
plt.grid(True, alpha=0.3)

plt.subplot(4, 1, 2)
plt.plot(t[:2000], y2[:2000], 'r-', linewidth=1)
plt.title(f'Wave 2: {f2} Hz')
plt.ylabel('Amplitude')
plt.grid(True, alpha=0.3)

# Resultant wave with beat pattern
plt.subplot(4, 1, 3)
plt.plot(t[:2000], y_resultant[:2000], 'g-', linewidth=1.5, label='Resultant')
plt.plot(t[:2000], beat_envelope[:2000], 'k--', linewidth=1, label='Beat Envelope')
plt.plot(t[:2000], -beat_envelope[:2000], 'k--', linewidth=1)
plt.title(f'Resultant Wave (Beat Frequency Δf = {delta_f} Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)

# Theoretical vs Actual comparison
plt.subplot(4, 1, 4)
plt.plot(t[:2000], y_resultant[:2000], 'g-', linewidth=1.5, alpha=0.7, label='Actual')
plt.plot(t[:2000], theoretical_beat[:2000], 'm-', linewidth=1, alpha=0.8, label='Theoretical')
plt.title('Comparison: Actual vs Theoretical Beat Pattern')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Additional analysis
print("\n=== BEAT PHENOMENA ANALYSIS ===")
print(f"Time period of beat (Tb): {1/delta_f:.4f} seconds")
print(f"Number of beats per second: {delta_f}")
print(f"Modulation frequency: {delta_f/2} Hz")

# Verify the beat mathematically
# The product-to-sum formula gives:
# sin(2πf1t) + sin(2πf2t) = 2cos(2π((f1-f2)/2)t) * sin(2π((f1+f2)/2)t)
print(f"\nMathematical verification:")
print(f"2cos(2π*({delta_f/2})t) * sin(2π*({f_avg})t)")