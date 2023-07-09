# import matplotlib.pyplot as plt

# def brasenhum(x0, y0, xn, yn):
#     delta_x = abs(xn - x0)
#     delta_y = abs(yn - y0)

#     p = 2 * delta_y - delta_x

#     x_step = 1 if x0 < xn else -1
#     y_step = 1 if y0 < yn else -1

#     x = x0
#     y = y0

#     points = []
    
#     while True:
#         points.append((x, y))
        
#         if x == xn and y == yn:
#             break
        
#         if p < 0:
#             p = p + 2 * delta_y
#             x = x + x_step
#         else:
#             p = p + 2 * delta_y - 2 * delta_x
#             x = x + x_step
#             y = y + y_step
    
#     return points

# # Define the line coordinates
# x1, y1 = 1, 1
# x2, y2 = 8, 5

# # Call the line drawing function
# line_points = brasenhum(x1, y1, x2, y2)

# # Print the points
# print("Line Points:")
# for point in line_points:
#     print(point)

# # Plot the line
# x_coords = [point[0] for point in line_points]
# y_coords = [point[1] for point in line_points]

# plt.plot(x_coords, y_coords, marker='o')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Bresenham Line Drawing')
# plt.grid(True)
# plt.show()





import matplotlib.pyplot as plt

def bresenham(x0, y0, xn, yn):
    delta_x = abs(xn - x0)
    delta_y = abs(yn - y0)

    p = 2 * delta_y - delta_x

    x_step = 1 if x0 < xn else -1
    y_step = 1 if y0 < yn else -1

    x = x0
    y = y0

    points = []
    
    while True:
        points.append((x, y))
        
        if x == xn and y == yn:
            break
        
        if p < 0:
            p = p + 2 * delta_y
            x = x + x_step
        else:
            p = p + 2 * delta_y - 2 * delta_x
            x = x + x_step
            y = y + y_step
    
    return points

# Define the line coordinates
x1, y1 = 1, 1
x2, y2 = 8, 5

# Call the line drawing function
line_points = bresenham(x1, y1, x2, y2)

# Print the points
print("Line Points:")
for point in line_points:
    print(point)

# Plot the line
x_coords = [point[0] for point in line_points]
y_coords = [point[1] for point in line_points]

plt.plot(x_coords, y_coords, 'r-', linewidth=2, marker='o', markersize=5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line Drawing')
plt.grid(True)
plt.show()

