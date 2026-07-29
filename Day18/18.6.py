from turtle import *
from random import *

def color_choosing():
    r = int(randint(1,254))
    g = int(randint(1,254))
    b = int(randint(1,254))
    return (r, g, b)

tim = Turtle()
tim.speed(0)
tim.pensize(15)
colormode(255)

ben = Turtle()
ben.speed(0)
ben.pensize(15)
colormode(255)

game = True
while game == True:


# Tim is completly and horrifically random
    # tim.pencolor(color_choosing())
    # lf_or_rt = [0, 1]
    # binary = choice(lf_or_rt)
    # if binary == 0:
    #     tim.lt(randint(0,360))
    # else:
    #     tim.rt(randint(0,360))
    # tim.fd(randint(1,50))


# While ben is just the mild version of tim but this was the challenge given by angela
    ben.pencolor(color_choosing())
    direction = [0, 90, 180, 270]
    lf_or_rt = [0, 1]
    binary = choice(lf_or_rt)
    if binary == 0:
        ben.lt(choice(direction))
    else:
        ben.rt(choice(direction))
    ben.fd(25)
