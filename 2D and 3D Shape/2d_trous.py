# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import axes3d



# # Torus parameters
# R = 5  # Major radius (distance from the center of the tube to the center of the torus)
# r = 2  # Minor radius (radius of the tube)

# # spare coordinate
# # Angles
# theta = np.linspace(0, 2 * np.pi, 100)
# phi = np.linspace(0, 2 * np.pi, 50)
# theta, phi = np.meshgrid(theta, phi)

# # Torus parametric equations
# x = (R + r * np.cos(theta)) * np.cos(phi)
# y = (R + r * np.cos(theta)) * np.sin(phi)
# z = r * np.sin(theta)


# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # 2D plot
# axes[0].set_title('2D')
# axes[0].set_xlabel('x')
# axes[0].set_ylabel('y')
# axes[0].axis('equal')
# axes[0].plot(x, y, 'g.')

# # 3D plot
# axes[1] = plt.subplot(122, projection='3d')
# axes[1].set_title('3D')
# axes[1].set_xlabel('x')
# axes[1].set_ylabel('y')
# axes[1].set_zlabel('z')
# axes[1].plot_surface(x, y, z, cmap='viridis')

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 100

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

Rx, r = 2, 1
x = (Rx + r*np.cos(theta)) * np.cos(phi)
y = (Rx + r*np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)

fig = plt.figure(figsize=(10, 5))

# 3D plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_zlim(-3, 3)
ax1.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax1.view_init(36, 26)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Torus')

# 2D plot
ax2 = fig.add_subplot(122)
ax2.set_aspect('equal')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.plot(x.flatten(), y.flatten(), 'k', linewidth=0.5)
ax2.set_title('2D Torus')

plt.tight_layout()
plt.show()
