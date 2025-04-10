import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

origin = np.array([0,0])
v1 = np.array([3,1])
v2 = np.array([-4, 6])

fig, ax = plt.subplots()
ax.quiver(*origin, *v1, color='b', scale=1, scale_units='xy', angles='xy', label= 'Vector 1 (3, 1)')
ax.quiver(*origin, *v2, color='r', scale=1, scale_units='xy', angles='xy', label= 'Vector 2 (-4, 6)')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid()
ax.legend()
ax.set_aspect('equal')
plt.show()

