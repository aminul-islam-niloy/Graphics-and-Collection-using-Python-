import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def create_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    img = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = x * (x_max - x_min) / (width - 1) + x_min
            imaginary = y * (y_max - y_min) / (height - 1) + y_min
            c = complex(real, imaginary)
            img[y, x] = mandelbrot(c, max_iter)
    return img

# Set the desired parameters for the fractal
width = 800
height = 800
x_min, x_max = -2.5, 1
y_min, y_max = -1, 1
max_iter = 100

# Generate the fractal image
fractal_img = create_fractal(width, height, x_min, x_max, y_min, y_max, max_iter)

# Display the fractal image
plt.imshow(fractal_img, cmap='hot', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.show()
