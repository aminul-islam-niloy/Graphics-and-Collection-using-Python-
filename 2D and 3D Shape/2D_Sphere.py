import matplotlib.pyplot as plt
import numpy as np

# spare coordinate
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)

radius = 1

# x = r * sin(phi) * cos(theta)
# y = r * sin(phi) * sin(theta)
# z = r * cos(phi)

x = radius * np.sin(phi) * np.cos(theta)
y = radius * np.sin(phi) * np.sin(theta)
z = radius * np.cos(phi)

# x = radius * np.cos(phi) * np.cos(theta)
# y = radius * np.cos(phi) * np.sin(theta)
# z = radius * np.sin(theta)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# 2D plot
axes[0].set_title('2D')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].axis('equal')
axes[0].plot(x, y, 'g.')

# 3D plot
axes[1] = plt.subplot(122, projection='3d')
axes[1].set_title('3D')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_zlabel('z')
axes[1].plot_surface(x, y, z, cmap='Blues')

plt.tight_layout()
plt.show()
