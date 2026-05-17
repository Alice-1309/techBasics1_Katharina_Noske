# import turtle
from turtle import *

# import random
import random

# parameters
width = 500
height = 500
size_star = 100
size_pentagon = 25
pen_color = "#191970"
star_color = "#CFB53B"
bg_color = "#191970"

def setup_canvas():
    setup(width, height) # set up
    tracer(0, 0)  # disable animation
    bgcolor(bg_color) # create a background color

# change start position to a random starting point
def move_to_star():
    penup()
    x = random.randrange(-width//2+size_star, width//2-size_star) # create a random starting point on x axis
    y = random.randrange(-height//2+size_star, height//2-size_star) # create a random starting point on y axis
    goto(x, y)
    pendown()
    return x, y  # giving the coordinates back

# coloring the star
def coloring_star():
    fillcolor(star_color)
    pencolor(pen_color)
    begin_fill()
    draw_star(size_star)
    end_fill()

# draw star
def draw_star(size_star):
    for _ in range(5):
        forward(size_star)
        left(144)

# move the start position for the pentagon
def move_to_pentagon(x, y):
    penup()
    goto(x + 37, y)
    pendown()

# coloring pentagon
def coloring_pentagon():
    fillcolor(star_color)
    pencolor(star_color)
    begin_fill()
    draw_pentagon(size_pentagon)
    end_fill()

# draw pentagon
def draw_pentagon(size_pentagon):
    for _ in range(5):
        forward(size_pentagon)
        left(72)



def main_design():
    for _ in range(7):
        x, y = move_to_star()
        coloring_star()
        draw_star(size_star)
        move_to_pentagon(x, y)
        coloring_pentagon()
        draw_pentagon(size_pentagon)

def main():
    setup_canvas()
    main_design()
    update()
    done()


if __name__ == "__main__":
    main()

# No matter what I did, I couldn't fill in the star completely so I decided to go with a pentagon witch I put inside the star...