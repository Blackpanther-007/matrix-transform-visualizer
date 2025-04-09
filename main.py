# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation 

# x = np.linspace(-10, 10,20)
# y = np.linspace(-10, 10,20)
# X,Y = np.meshgrid(x,y)

# U = -Y
# V = X


# plt.quiver(X,Y,U,V, scale=100, color='green', width=0.005)
# plt.xlim(-10,10)
# plt.ylim(-10,10)
# plt.grid()
# plt.show()

#animation 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

g = 9.8
angle = np.pi/4
vo = 40
t_max = 2 * vo * np.sin(angle) / g

fig, ax = plt.subplots()
line, = ax.plot([], [], 'ro')  # This plots a red dot initially
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Initialize the plot
def init():
    line.set_data([], [])
    return line,

# Update the plot for each frame
def update(t):
    x = vo * np.cos(angle) * t
    y = vo * np.sin(angle) * t - 0.5 * g * t**2
    line.set_data(x, y)  # Update position of the single point
    return line,

# Create the animation
ani = FuncAnimation(fig, func=update, frames=np.linspace(0, t_max, 100), init_func=init, blit=True, interval=20)

plt.grid()
plt.show()
