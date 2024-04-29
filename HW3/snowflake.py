import turtle

# Constants
COLORMODE = 255
BG_COLOR = (201, 143, 135)
LINE_COLOR = "#4f9c95"
ANGLE = 60

# Set up the screen
turtle.colormode(COLORMODE)
screen = turtle.Screen()
screen.bgcolor(BG_COLOR)

# Set up the turtle
koch_turtle = turtle.Turtle()
koch_turtle.speed(10)
koch_turtle.penup()
koch_turtle.pensize(2)
koch_turtle.goto(-150, 90)
koch_turtle.pendown()
koch_turtle.color(LINE_COLOR)

def draw_koch_line(length):
    koch_turtle.forward(length)

def draw_koch_curve(length, depth):
    if depth == 0:
        draw_koch_line(length)
    else:
        draw_koch_curve(length / 3, depth - 1)
        koch_turtle.left(ANGLE)
        draw_koch_curve(length / 3, depth - 1)
        koch_turtle.right(2 * ANGLE)
        draw_koch_curve(length / 3, depth - 1)
        koch_turtle.left(ANGLE)
        draw_koch_curve(length / 3, depth - 1)

def create_koch_snowflake(length, depth):
    for _ in range(3):
        draw_koch_curve(length, depth)
        koch_turtle.right(120)

create_koch_snowflake(172, 1)
turtle.done()