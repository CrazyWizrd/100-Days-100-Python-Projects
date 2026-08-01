from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.ht()
        self.penup()
        self.teleport(0, 260)
        self.color("white")
        self.score_update()

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
