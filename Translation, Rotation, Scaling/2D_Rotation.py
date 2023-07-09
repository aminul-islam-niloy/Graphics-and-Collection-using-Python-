# import matplotlib.pyplot as plt
# import numpy as np
# import math

# #points(x,y)
# points = np.array([[3,3], [3,6], [6,6], [6,3], [3,3]])

# def rotate(points, angle):
#     red_angle = math.radians(angle)
#     rotation_matrix = np.array([[math.cos(red_angle), -math.sin(red_angle)],
#                                 [math.sin(red_angle), math.cos(red_angle)]])
  
#     rotated_points = np.dot(points, rotation_matrix)
#     return rotated_points

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # Original Image
# axes[0].plot(points[:, 0], points[:, 1], 'ro-')
# axes[0].set_title('Original')
# axes[0].set_xlim(-10, 10)
# axes[0].set_ylim(-10, 10)
# axes[0].set_aspect('equal', adjustable='box')

# rotated_points = rotate(points, 45)  # Rotate the points by 45 degrees
# axes[1].plot(rotated_points[:, 0], rotated_points[:, 1], 'go-')
# axes[1].set_title('Rotation')
# axes[1].set_xlim(-10, 10)
# axes[1].set_ylim(-10, 10)
# axes[1].set_aspect('equal', adjustable='box')

# plt.show()




import matplotlib.pyplot as plt
import numpy as np

# Points (x, y)
points = np.array([[3, 3], [6, 6], [3, 6], [3, 3]])  # Triangle vertices

def rotate(points, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    rotated_points = np.dot(points, rotation_matrix)
    return rotated_points

fig, axes = plt.subplots(1, 2, figsize=(10, 10 ))

# Original Image
axes[0].fill(points[:, 0], points[:, 1], color='red', alpha=0.3)
axes[0].plot(points[:, 0], points[:, 1], 'ro-')
axes[0].set_title('Original')
axes[0].set_xlim(0, 10)
axes[0].set_ylim(0, 10)
axes[0].set_aspect('equal', adjustable='box')
axes[0].axhline(0, color='black', linewidth=0.5)
axes[0].axvline(0, color='black', linewidth=0.5)

rotated_points = rotate(points, 25)
axes[1].fill(rotated_points[:, 0], rotated_points[:, 1], color='green', alpha=0.3)
axes[1].plot(rotated_points[:, 0], rotated_points[:, 1], 'go-')
axes[1].set_title('Rotated')
axes[1].set_xlim(0, 10)
axes[1].set_ylim(0, 10)
axes[1].set_aspect('equal', adjustable='box')
axes[1].axhline(0, color='black', linewidth=0.5)
axes[1].axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()

