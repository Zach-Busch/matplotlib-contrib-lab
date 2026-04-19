"""Sensor scatter plot example.

This example demonstrates how to generate synthetic sensor data with NumPy
and visualize two sensor signals over time using a scatter plot. It is useful
for engineers who want a simple way to compare noisy measurements.
"""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1234)
n = 200
time = rng.uniform(0, 10, n)
sensor_a = rng.normal(25, 3, n)
sensor_b = rng.normal(27, 4.5, n)

fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(time, sensor_a, alpha=0.7, label="Sensor A")
ax.scatter(time, sensor_b, alpha=0.7, label="Sensor B")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Sensor Readings Over Time")
ax.legend()
ax.grid(True)

plt.show()

# .. admonition:: References
#
#    - matplotlib.pyplot.scatter
#    - matplotlib.pyplot.subplots
#
# .. tags::
#
#    plot-type: scatter
#    level: beginner