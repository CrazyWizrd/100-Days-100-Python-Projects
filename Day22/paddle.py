from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.seth(90)
        self.shapesize(1, 5)
        self.goto(position)

    def go_up(self):
        self.fd(25)

    def go_down(self):
        self.bk(25)
