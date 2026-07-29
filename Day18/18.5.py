from turtle import *
from random import *

def color_choosing(sides):
    color_list = []
    for _ in range(sides):
        r = int(randint(1,254))
        g = int(randint(1,254))
        b = int(randint(1,254))
        color_list.append((r,g,b))
    return color_list

def setup():
    tim.penup()
    tim.lt(90)
    tim.fd(300)
    tim.lt(90)
    tim.fd(50)
    tim.right(180)
    tim.pendown()

def shape_maker(turtle, sides, color_list):
    list_data = 0
    for shape in range(3,sides+1):
        angle = 360/shape
        turtle.pencolor(color_list[list_data])
        list_data += 1
        for _ in range(shape):
            turtle.fd(100)
            turtle.rt(angle)



tim = Turtle()
colormode(255)
setup()
number_of_sides = int(input("Till how many sides you want program to draw: "))
color_code = color_choosing(number_of_sides)
shape_maker(tim, number_of_sides, color_code)

screen = Screen()
screen.exitonclick()