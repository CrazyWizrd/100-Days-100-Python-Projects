from turtle import *

def move_fd():
    jim.fd(10)

jim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move_fd)
screen.exitonclick()
