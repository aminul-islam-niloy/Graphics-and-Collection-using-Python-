import matplotlib.pyplot as plt
import numpy as np


def bezier_curve(control_points, num_points):
    t = np.linspace(0, 1, num_points)
    n = len(control_points) - 1
    curve_points = []

    for i in range(num_points):
        b = sum(
            [
                control_points[j] * binomial_coefficient(n, j) * (1 - t[i]) ** (n - j) * t[i] ** j
                for j in range(n + 1)
            ]
        )
        curve_points.append(b)

    return curve_points


def binomial_coefficient(n, i):
    return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))


# Example control points
control_points = np.array([[0, 0],[2,5], [5, 3], [6, 6]])

# Number of points on the curve
num_points = 100

# Calculate Bezier curve points
curve_points = bezier_curve(control_points, num_points)

# Extract x and y coordinates from curve points
x_coords = [point[0] for point in curve_points]
y_coords = [point[1] for point in curve_points]


# Plot the Bezier curve
plt.plot(x_coords, y_coords, 'b', label='Bezier Curve')
plt.scatter(control_points[:, 0], control_points[:, 1], color='red', label='Control Points')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bezier Curve')
plt.grid(True)
plt.show()
