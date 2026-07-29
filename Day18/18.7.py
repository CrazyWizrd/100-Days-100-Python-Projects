from turtle import *
from random import *

def color_choosing():
    r = int(randint(1,254))
    g = int(randint(1,254))
    b = int(randint(1,254))
    return (r, g, b)

tim = Turtle()
colormode(255)
tim.speed(0)

circles = int(input("How many circles you want? (72 recommended): "))
angle = 0
for num in range (circles):
    add_angle = 360/circles
    tim.pencolor(color_choosing())
    tim.lt(angle)
    tim.circle(100)
    angle += add_angle
    tim.home()

screen = Screen()
screen.exitonclick()
