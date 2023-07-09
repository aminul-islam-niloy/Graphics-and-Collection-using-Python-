# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import axes3d

# # spare coordinate

# theta = np.linspace(0, 2 * np.pi, 100)
# # 100 equally spaced values between 0 and 2π
# # represents the azimuthal angle in a spherical coordinate system
# phi = np.linspace(0, np.pi, 50)
# # 50 equally spaced values between 0 and π
# # epresents the polar angle in a spherical coordinate system

# theta, phi = np.meshgrid(theta, phi)
# # creates a grid of coordinates by combining the values




# radius1 = 2
# radius2 = 1
# radius3 = 1


# # x = r * sin(phi) * cos(theta)
# # y = r * sin(phi) * sin(theta)
# # z = r * cos(phi)

# x = radius1 * np.sin(phi) * np.cos(theta)
# y = radius2 * np.sin(phi) * np.sin(theta)
# z = radius3 * np.cos(phi)

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







import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate ellipsoid coordinates
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi,50)
theta, phi = np.meshgrid(theta, phi)

a = 2  # x-axis radius
b = 1  # y-axis radius
c = 1  # z-axis radius

x = a * np.sin(phi) * np.cos(theta)
y = b * np.sin(phi) * np.sin(theta)
z = c * np.cos(phi)

# Calculate the maximum radius of the ellipsoid
max_radius = max(a, b, c)

# Plot the ellipsoid in 2D
plt.subplot(121)
plt.title('Ellipsoid (2D)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)
plt.plot(x, y, 'g.')

# Plot the ellipsoid in 3D
ax = plt.subplot(122, projection='3d')
ax.set_title('Ellipsoid (3D)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set limit of all three axes to the maximum radius
ax.set_xlim(-max_radius, max_radius)
ax.set_ylim(-max_radius, max_radius)
ax.set_zlim(-max_radius, max_radius)

ax.plot_surface(x, y, z, cmap='viridis')

# Display the plots
plt.tight_layout()
plt.show()


