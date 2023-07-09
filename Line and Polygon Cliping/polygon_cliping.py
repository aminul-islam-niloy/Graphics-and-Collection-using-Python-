# import matplotlib.pyplot as plt

# # Function to perform polygon clipping
# def clip(subject_polygon, frame):
#     # Function to check if a point is inside an edge
#     def is_inside(p, cp1, cp2):
#         return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0])

#     # Function to calculate the intersection point
#     def calculate_intersection(cp1, cp2, s, e):
#         dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
#         dp = [s[0] - e[0], s[1] - e[1]]
#         n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
#         n2 = s[0] * e[1] - s[1] * e[0]
#         n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
#         return [(n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3]

#     # Make a copy of the subject polygon
#     output_list = subject_polygon.copy()
#     cp1 = frame[-1]  # Last point of the clip polygon
#     for cp2 in frame:
#         input_list = output_list
#         output_list = []
#         s = input_list[-1]  # Last point of the subject polygon
#         for e in input_list:
#             if is_inside(e, cp1, cp2):  # Check if point e is inside the edge formed by cp1 and cp2
#                 if not is_inside(s, cp1, cp2):  # Check if point s is outside the edge formed by cp1 and cp2
#                     output_list.append(calculate_intersection(cp1, cp2, s, e))  # Add intersection point to output
#                 output_list.append(e)  # Add point e to output
#             elif is_inside(s, cp1, cp2):  # Check if point s is inside the edge formed by cp1 and cp2
#                 output_list.append(calculate_intersection(cp1, cp2, s, e))  # Add intersection point to output
#             s = e
#         cp1 = cp2

#     return output_list

# # Create a subject polygon (triangle shape)
# subject_polygon = [(-0.5, -1), (0.5, -1), (0, 1)]

# # Define the rectangular frame
# frame = [(-1.5, -1.5), (1.5, -1.5), (1.5, 1.5), (-1.5, 1.5)]

# # Call the clip function to obtain the output polygon
# output_polygon = clip(subject_polygon, frame)

# # Extract the x and y coordinates of the output polygon
# output_x = [point[0] for point in output_polygon]
# output_y = [point[1] for point in output_polygon]

# # Plot the subject polygon
# subject_x = [point[0] for point in subject_polygon]
# subject_y = [point[1] for point in subject_polygon]
# plt.plot(subject_x + [subject_x[0]], subject_y + [subject_y[0]], 'b-', label='Subject Polygon')

# # Plot the clip polygon
# frame_x = [point[0] for point in frame]
# frame_y = [point[1] for point in frame]
# plt.plot(frame_x + [frame_x[0]], frame_y + [frame_y[0]], 'r-', label='Frame')

# # Plot the output polygon
# plt.plot(output_x + [output_x[0]], output_y + [output_y[0]], 'g-', label='Output Polygon')

# # Add labels and title to the plot
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Polygon Clipping')
# plt.grid(True)

# # Display the plot
# plt.show()



import matplotlib.pyplot as plt

def polygon_clipping(subject_polygon, frame):
    def is_inside(point, edge_start, edge_end):
        # Check if a point is inside an edge
        edge_slope = (edge_end[0] - edge_start[0]) * (point[1] - edge_start[1])
        point_slope = (edge_end[1] - edge_start[1]) * (point[0] - edge_start[0])
        return edge_slope > point_slope

    def calculate_intersection(edge_start, edge_end, segment_start, segment_end):
        # Calculate the intersection point of two line segments
        edge_diff = [edge_start[0] - edge_end[0], edge_start[1] - edge_end[1]]
        segment_diff = [segment_start[0] - segment_end[0], segment_start[1] - segment_end[1]]
        n1 = edge_start[0] * edge_end[1] - edge_start[1] * edge_end[0]
        n2 = segment_start[0] * segment_end[1] - segment_start[1] * segment_end[0]
        n3 = 1.0 / (edge_diff[0] * segment_diff[1] - edge_diff[1] * segment_diff[0])
        return [(n1 * segment_diff[0] - n2 * edge_diff[0]) * n3, (n1 * segment_diff[1] - n2 * edge_diff[1]) * n3]

    output_polygon = subject_polygon.copy()
    previous_edge_end = frame[-1]
    for current_edge_end in frame:
        input_polygon = output_polygon
        output_polygon = []
        previous_segment_end = input_polygon[-1]
        for current_segment_end in input_polygon:
            if is_inside(current_segment_end, previous_edge_end, current_edge_end):
                if not is_inside(previous_segment_end, previous_edge_end, current_edge_end):
                    intersection_point = calculate_intersection(previous_edge_end, current_edge_end, previous_segment_end, current_segment_end)
                    output_polygon.append(intersection_point)
                output_polygon.append(current_segment_end)
            elif is_inside(previous_segment_end, previous_edge_end, current_edge_end):
                intersection_point = calculate_intersection(previous_edge_end, current_edge_end, previous_segment_end, current_segment_end)
                output_polygon.append(intersection_point)
            previous_segment_end = current_segment_end
        previous_edge_end = current_edge_end

    return output_polygon

# Create a subject polygon (triangle shape)
subject_polygon = [(0, -2), (2, -2), (1, 2)]

# Define the rectangular frame
frame = [(-1.5, -1.5), (1.5, -1.5), (1.5, 1.5), (-1.5, 1.5)]

# Perform polygon clipping
output_polygon = polygon_clipping(subject_polygon, frame)

# Extract the x and y coordinates of the output polygon
output_x = [point[0] for point in output_polygon]
output_y = [point[1] for point in output_polygon]

# Plot the subject polygon
subject_x = [point[0] for point in subject_polygon]
subject_y = [point[1] for point in subject_polygon]
plt.plot(subject_x + [subject_x[0]], subject_y + [subject_y[0]], 'b-', label='Subject Polygon')

# Plot the clip polygon
frame_x = [point[0] for point in frame]
frame_y = [point[1] for point in frame]
plt.plot(frame_x + [frame_x[0]], frame_y + [frame_y[0]], 'r-', label='Frame')

# Plot the output polygon
plt.plot(output_x + [output_x[0]], output_y + [output_y[0]], 'g-', label='Output Polygon')

# Add labels and title to the plot
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon Clipping')
plt.grid(True)

# Display the plot
plt.show()


import matplotlib.pyplot as plt

def polygon_clipping(subject_polygon, frame):
    def is_inside(point, edge_start, edge_end):
        # Check if a point is inside an edge
        edge_slope = (edge_end[0] - edge_start[0]) * (point[1] - edge_start[1])
        point_slope = (edge_end[1] - edge_start[1]) * (point[0] - edge_start[0])
        return edge_slope > point_slope

    def calculate_intersection(edge_start, edge_end, segment_start, segment_end):
        # Calculate the intersection point of two line segments
        edge_diff = [edge_start[0] - edge_end[0], edge_start[1] - edge_end[1]]
        segment_diff = [segment_start[0] - segment_end[0], segment_start[1] - segment_end[1]]
        n1 = edge_start[0] * edge_end[1] - edge_start[1] * edge_end[0]
        n2 = segment_start[0] * segment_end[1] - segment_start[1] * segment_end[0]
        n3 = 1.0 / (edge_diff[0] * segment_diff[1] - edge_diff[1] * segment_diff[0])
        return [(n1 * segment_diff[0] - n2 * edge_diff[0]) * n3, (n1 * segment_diff[1] - n2 * edge_diff[1]) * n3]

    output_polygon = subject_polygon.copy()
    previous_edge_end = frame[-1]
    for current_edge_end in frame:
        input_polygon = output_polygon
        output_polygon = []
        previous_segment_end = input_polygon[-1]
        for current_segment_end in input_polygon:
            if is_inside(current_segment_end, previous_edge_end, current_edge_end):
                if not is_inside(previous_segment_end, previous_edge_end, current_edge_end):
                    intersection_point = calculate_intersection(previous_edge_end, current_edge_end, previous_segment_end, current_segment_end)
                    output_polygon.append(intersection_point)
                output_polygon.append(current_segment_end)
            elif is_inside(previous_segment_end, previous_edge_end, current_edge_end):
                intersection_point = calculate_intersection(previous_edge_end, current_edge_end, previous_segment_end, current_segment_end)
                output_polygon.append(intersection_point)
            previous_segment_end = current_segment_end
        previous_edge_end = current_edge_end

    return output_polygon

# Create a subject polygon (triangle shape)
subject_polygon = [(-0.5, -1), (0.5, -1), (0, 1)]

# Define the rectangular frame
frame = [(-1.5, -1.5), (1.5, -1.5), (1.5, 1.5), (-1.5, 1.5)]

# Perform polygon clipping
output_polygon = polygon_clipping(subject_polygon, frame)

# Extract the x and y coordinates of the output polygon
output_x = [point[0] for point in output_polygon]
output_y = [point[1] for point in output_polygon]

# Plot the subject polygon
subject_x = [point[0] for point in subject_polygon]
subject_y = [point[1] for point in subject_polygon]
plt.plot(subject_x + [subject_x[0]], subject_y + [subject_y[0]], 'b-', label='Subject Polygon')

# Plot the clip polygon
frame_x = [point[0] for point in frame]
frame_y = [point[1] for point in frame]
plt.plot(frame_x + [frame_x[0]], frame_y + [frame_y[0]], 'r-', label='Frame')

# Plot the output polygon
plt.plot(output_x + [output_x[0]], output_y + [output_y[0]], 'g-', label='Output Polygon')

# Add labels and title to the plot
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon Clipping')
plt.grid(True)

# Display the plot
plt.show()

