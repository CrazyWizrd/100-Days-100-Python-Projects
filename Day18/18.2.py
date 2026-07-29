# Turtle challenge 1 - Draw a square
from turtle import *
timmy = Turtle()

# Best and optimal Solution
# for _ in range(0,4):
#     timmy.fd(100)
#     timmy.rt(90)

#lenghty visually better solution
timmy.penup()
timmy.fd(50)
timmy.right(90)
timmy.pendown()
timmy.fd(50)
for _ in range(0,3):
    timmy.right(90)
    timmy.fd(100)
timmy.right(90)
timmy.fd(50)

screen = Screen()
screen.exitonclick()
