from turtle import *

def fd():
    tim.fd(10)
def bk():
    tim.bk(10)
def lt():
    head = tim.heading()
    tim.setheading(head+10)
def rt():
    head = tim.heading()
    tim.setheading(head-10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(fd,"w")
screen.onkey(bk,"s")
screen.onkey(lt,"a")
screen.onkey(rt,"d")
screen.onkey(clear,"c")
screen.exitonclick()
