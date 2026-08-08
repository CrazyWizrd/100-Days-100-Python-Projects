FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 240)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, -20)
        self.write("GAME OVER", False, "center", FONT)

