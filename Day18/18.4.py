from turtle import Turtle, Screen
tim = Turtle()
for _ in range(35):
    tim.fd(5)
    tim.penup()
    tim.fd(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()
