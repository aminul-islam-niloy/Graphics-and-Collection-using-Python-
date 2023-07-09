import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# (x / a) ^ n1 + (y / b) ^ n2 + (z / c) ^ n3 = 1

# (x, y, z) are the coordinates of a point on the surface of the superellipsoid.
# (a, b, c) are the radii of the superellipsoid along the x-axis, y-axis, and z-axis, respectively.
# (n1, n2, n3) are the exponents that control the shape of the superellipsoid along the respective axes.


# Set up the parameters
Rx = 100  # x-axis radius
Ry = 100  # y-axis radius
Rz = 100  # z-axis radius

e1 = 2   # exponent for x-axis
e2 = 2   # exponent for y-axis
e3 = 2   # exponent for z-axis

# Set up the transformation variables
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)

# Calculate the vertices of the superellipsoid
x = np.outer(np.cos(theta), np.sin(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.ones(np.size(theta)), np.cos(phi))

x = Rx * np.sign(x) * np.power(np.abs(x), e1)
y = Ry * np.sign(y) * np.power(np.abs(y), e2)
z = Rz * np.sign(z) * np.power(np.abs(z), e3)

# Plot the Superellipsoid in 2D and 3D side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the Superellipsoid in 2D
axes[0].contourf(x, y, levels=100, cmap='plasma')
axes[0].set_xlabel('X-axis')
axes[0].set_ylabel('Y-axis')
axes[0].set_title('Superellipsoid (2D)')

# Plot the Superellipsoid in 3D
axes[1] = fig.add_subplot(122, projection='3d')
axes[1].plot_surface(x, y, z, cmap='magma')
axes[1].set_xlabel('X-axis')
axes[1].set_ylabel('Y-axis')
axes[1].set_zlabel('Z-axis')
axes[1].set_title('Superellipsoid (3D)')

plt.tight_layout()
plt.show()