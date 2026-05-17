# import turtle
from turtle import *

# import random
import random

# parameters
width = 500 # size of canvas (-250, 250)
height = 800 # size of canvas (-400, 400)
size = 40 # size of square
noise = 1

# first step: set up
setup(width, height)

# disable animation
tracer(0,0)

# for-loop to shift the square along the y-axis
for y in range(18):
    # for-loop to shift the square along the x-axis
    for x in range(12):
        # move starting point
        penup()
        goto(-width/2+x*size, height/2-y*size)
        pendown()
        # rotate
        angle = random.uniform(-noise, noise)
        right(angle) # move the original direction
        # draw square
        for i in range(4):
            forward(size)  # draw from starting point, go forward
            right(90)  # turn right 90°
        left(angle) # move back the original direction
    #end of a row
    noise += 3

# done drawing
penup()

# import to keep at the end
done()