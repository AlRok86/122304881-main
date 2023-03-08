"""
import turtle

def draw_hexagon(side_length):
    for i in range(6):
        turtle.forward(side_length)
        turtle.right(60)

turtle.speed(10)

for i in range(1):
    draw_hexagon(100)
    turtle.right(60)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

turtle.done()
"""

import turtle
import math

def draw_hexagon(side_length):
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(side_length)
        turtle.right(60)
    turtle.end_fill()

turtle.speed(0)
turtle.penup()

side_length = 30
shift = math.sqrt(side_length**2 * 3.0 /4.0)

x = 0
y = 0

# Calculate the number of hexagons that can fit in the window
#rows = int((turtle.window_height() - side_length) / (1.5 * side_length))
#cols = int((turtle.window_width() - side_length) / (side_length * 2))

rows = 5
cols = 5

for row in range(0, 10):
    x = 0
    if row % 2 == 0:
        x = side_length * 3.0/2.0
    for col in range(0, 5):
        turtle.setpos(x, y)
        turtle.pendown()
        turtle.fillcolor("red")
        draw_hexagon(side_length)
        turtle.penup()
        x += side_length * 3
    y -= shift

turtle.done()
