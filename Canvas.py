import turtle
import math 

screen = turtle.Screen()
screen.setup(width=600, height=600)

# Hide default turtle
t = turtle.Turtle()
screen.bgcolor("#017B92")
t.speed(0)
t.pencolor('white')
t.hideturtle()
t.penup()

# List of colors for stripes
colors = ["#F8CCC5", "#F0AAA0","#659FAA", "#017B92"]
stripe_height = 600 // len(colors)  # height of each color stripe

# Start drawing stripes from top
start_y = 300

# Function to draw a filled rectangle
def draw_rect(color, y):
    t.goto(-300, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(600)
        t.right(90)
        t.forward(stripe_height)
        t.right(90)
    t.end_fill()
    t.penup()

# Function to draw a wave
def draw_wave(y, color):
    t.fillcolor(color)
    t.pencolor(color)
    t.goto(-300, y)
    t.pendown()
    t.begin_fill()

    # Draw sine-like wave across screen
    for x in range(-300, 301, 10):
        wave_y = y + 10 * math.sin((x + 300) * 0.05)
        t.goto(x, wave_y)

    # Close the wave shape (bottom edge)
    t.goto(300, y - stripe_height)
    t.goto(-300, y - stripe_height)
    t.goto(-300, y)
    t.end_fill()
    t.penup()

def drawSun(radius = 100):
    t.pencolor('#DD8F47')
    t.fillcolor('#DD8F47')
    t.penup()
    t.goto(-100,150)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw top 5 solid stripes
for i in range(len(colors) - 2):
    draw_rect(colors[i], start_y)
    start_y -= stripe_height
# Draw bottom 2 wavy stripes
draw_wave(start_y + 10, colors[-2])
start_y -= (stripe_height - 30)
draw_wave(start_y, colors[-1])
drawSun()
turtle.done()

