import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Physics setup
g = 9.8
angle = np.pi/4  # 45 degrees
vo = 40
t_max = 2 * vo * np.sin(angle) / g  # Time until projectile hits ground
t_values = np.linspace(0, t_max, 100)  # Time steps

# Trajectory calculations
x_values = vo * np.cos(angle) * t_values
y_values = vo * np.sin(angle) * t_values - 0.5 * g * t_values**2

# Plot setup
fig, ax = plt.subplots()
line, = ax.plot([], [], 'ro')  # Red dot for current position
trail, = ax.plot([], [], 'b-', alpha=0.5)  # Blue line for trajectory
ax.set_xlim(0, max(x_values) + 10)
ax.set_ylim(0, max(y_values) + 10)
ax.grid()

# Initialize animation
def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail

# Update animation frame
def update(i):
    line.set_data([x_values[i]], [y_values[i]])  # Wrap in lists!
    trail.set_data(x_values[:i+1], y_values[:i+1])
    return line, trail

# Create animation
ani = FuncAnimation(
    fig, 
    update, 
    frames=len(t_values), 
    init_func=init, 
    blit=True, 
    interval=20, 
    repeat=False
)

plt.title("Projectile Motion Animation")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.show()