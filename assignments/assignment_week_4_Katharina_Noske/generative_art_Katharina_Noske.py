# import turtle
from encodings import raw_unicode_escape
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

# set up
setup(width, height)

# disable animation
tracer(0, 0)

# create a background color
bgcolor(bg_color)

# change start position to a random starting point
for _ in range(7):
    penup()
    x = random.randrange(-width//2+size_star, width//2-size_star)
    y = random.randrange(-height//2+size_star, height//2-size_star)
    goto(x, y)
    pendown()

    # coloring star
    fillcolor(star_color)
    pencolor(pen_color)
    begin_fill()

    # draw star
    for _ in range(5):
        forward(size_star)
        left(144)

    # end coloring the star
    end_fill()

    penup()
    goto(x + 37, y)
    pendown()

    # coloring star
    fillcolor(star_color)
    pencolor(star_color)
    begin_fill()

    # draw pentagon
    for _ in range(5):
        forward(size_pentagon)
        left(72)

    # end coloring the pentagon
    end_fill()

# done drawing
penup()

# import to keep at the end
done()



# No matter what I did, I couldn't fill in the star completely so I decided to go with a pentagon witch I put inside the star...