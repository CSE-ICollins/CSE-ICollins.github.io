import numpy as np
import matplotlib.pyplot as plt

# Parameters
C = 5
D = 5
b = 1

# Time array from 0 to 2 seconds
t = np.linspace(0, 2, 400)
T = 100 + C * np.cos(2 * np.pi * b * t) + D * np.sin(2 * np.pi * t)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(t, T, label=r'$T(t) = 100 + 5 \cos(2 \pi t) + 5 \sin(2 \pi t)$')
plt.title('Temperature vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.axhline(y=100, color='r', linestyle='--', label='Baseline Temperature (100°C)')
plt.legend()
plt.grid()
plt.ylim(90, 110)  # Adjust y-limits for better visibility
plt.show()
