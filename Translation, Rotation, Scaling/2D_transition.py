# import matplotlib.pyplot as plt
# import numpy as np
# import math

# #points(x,y)
# points = np.array([[3,3], [3,6], [6,6], [6,3], [3,3]])

# def translate(points, tx, ty):
#     translated_points = points + np.array([tx, ty])
#     return translated_points

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # Original Image
# axes[0].plot(points[:, 0], points[:, 1], 'ro-')
# axes[0].set_title('Original')
# axes[0].set_xlim(0, 10)
# axes[0].set_ylim(0, 10)
# axes[0].set_aspect('equal', adjustable='box')

# translated_points = translate(points, 2, 3)
# axes[1].plot(translated_points[:, 0], translated_points[:, 1], 'go-')
# axes[1].set_title('Translated')
# axes[1].set_xlim(0, 10)
# axes[1].set_ylim(0, 10)
# axes[1].set_aspect('equal', adjustable='box')

# plt.tight_layout()
# plt.show()



#triangle 

# import matplotlib.pyplot as plt
# import numpy as np

# # Points (x, y)
# points = np.array([[3, 3], [6, 6], [3, 6], [3, 3]])  # Triangle vertices

# def translate(points, tx, ty):
#     translated_points = points + np.array([tx, ty])
#     return translated_points

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # Original Image
# axes[0].plot(points[:, 0], points[:, 1], 'ro-')
# axes[0].set_title('Original')
# axes[0].set_xlim(0, 10)
# axes[0].set_ylim(0, 10)
# axes[0].set_aspect('equal', adjustable='box')

# translated_points = translate(points, 2, 3)
# axes[1].plot(translated_points[:, 0], translated_points[:, 1], 'go-')
# axes[1].set_title('Translated')
# axes[1].set_xlim(0, 10)
# axes[1].set_ylim(0, 10)
# axes[1].set_aspect('equal', adjustable='box')

# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Points (x, y)
points = np.array([[2, 2], [4, 4], [6, 2], [2, 2]])  # Triangle vertices

def translate(points, tx, ty):
    translated_points = points + np.array([tx, ty])
    return translated_points

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Original Image
axes[0].fill(points[:, 0], points[:, 1], color='red', alpha=0.3)
axes[0].plot(points[:, 0], points[:, 1], 'ro-')
axes[0].set_title('Original')
axes[0].set_xlim(0, 10)
axes[0].set_ylim(0, 10)
axes[0].set_aspect('equal', adjustable='box')
axes[0].grid(True)
axes[0].axhline(0, color='black', linewidth=0.5)
axes[0].axvline(0, color='black', linewidth=0.5)

translated_points = translate(points, 2, 3)
axes[1].fill(translated_points[:, 0], translated_points[:, 1], color='green', alpha=0.3)
axes[1].plot(translated_points[:, 0], translated_points[:, 1], 'go-')
axes[1].set_title('Translated')
axes[1].set_xlim(0, 10)
axes[1].set_ylim(0, 10)
axes[1].grid(True)
axes[1].set_aspect('equal', adjustable='box')
axes[1].axhline(0, color='black', linewidth=0.5)
axes[1].axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()



