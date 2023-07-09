import matplotlib.pyplot as plt

def plot_points(x, y, xc, yc):
    """
    Plot the points of the circle using symmetry.
    """
    plt.plot(xc + x, yc + y, 'ro')
    plt.plot(xc - x, yc + y, 'ro')
    plt.plot(xc + x, yc - y, 'ro')
    plt.plot(xc - x, yc - y, 'ro')
    
    plt.plot(xc + y, yc + x, 'ro')
    plt.plot(xc - y, yc + x, 'ro')
    plt.plot(xc + y, yc - x, 'ro')
    plt.plot(xc - y, yc - x, 'ro')

def midpoint_circle(xc, yc, r):
    """
    Draw a circle using the Midpoint Circle Drawing Algorithm.
    """
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter

    # Plot the first point
    plot_points(x, y, xc, yc)

    while x < y:
        if p < 0:
            x = x + 1
            y = y
            p = p + 2 * x + 1
        else:
            x = x + 1
            y = y - 1
            p = p - 2 * (x - y) + 1

        # Plot the points
        plot_points(x, y, xc, yc)

    plt.axis('equal')  # Set aspect ratio to be equal
    plt.show()

# Example usage
# x_center = 0
# y_center = 0
# radius = 5

# Example usage
x_center = int(input("Enter the x-coordinate of the center: "))
y_center = int(input("Enter the y-coordinate of the center: "))
radius = int(input("Enter the radius of the circle: "))

midpoint_circle(x_center, y_center, radius)



#point_color = input("Enter the color of the plotted points (e.g., 'ro' for red circles): ")


