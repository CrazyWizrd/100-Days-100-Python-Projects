from turtle import *
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snakes()
        self.head = self.segments[0]

    def create_snakes(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.seth(0)
