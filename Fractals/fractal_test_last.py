from turtle import *
import turtle as tur

ws = tur.Screen()

def drawoval(rad):
    tur.pensize(5)  # Increase the pen size to make the circle bold
    for i in range(2):
        tur.circle(rad, 90)
        tur.circle(rad // 2, 90)

ws.setup(500, 500)
ws.bgcolor('black')

col = ['cyan', 'blue', 'pink', 'purple', 'yellow', 'green']

value = 15  # Adjust the initial angle for better alignment
index = 0

tur.speed(100)

for i in range(24):  # Draw 24 smaller circles
    tur.seth(-value)
    tur.color(col[index])
    drawoval(160)  # Increase the radius to make the circle bigger
    tur.penup()
    tur.goto(0, 0)  # Move back to the center
    tur.pendown()
    value += 15  # Adjust the angle for better alignment
    if index == 5:
        index = 0
    else:
        index += 1

tur.hideturtle()
tur.done()
