import turtle

def draw_koch(length, depth):
    if depth == 0:
        # Base case: draw a straight line
        turtle.forward(length)
    else:
        # Recursive case: draw four smaller Koch curves
        draw_koch(length / 3, depth - 1)
        turtle.left(60)
        draw_koch(length / 3, depth - 1)
        turtle.right(120)
        draw_koch(length / 3, depth - 1)
        turtle.left(60)
        draw_koch(length / 3, depth - 1)

# Set up the turtle graphics window
turtle.speed(0)  # Fastest speed
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()

# Call the function to draw the Koch snowflake
for _ in range(3):
    draw_koch(400, 4)
    turtle.right(120)

# Keep the window open until it is manually closed
turtle.done()
