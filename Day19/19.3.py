from turtle import *
from random import *

screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="Who do you think is going to Win!!", prompt="Who will win? (Jimmy/Kim/Howard/Nacho/Charles/Lalo):").lower()
x = -270
y = -125
turtles = [ "Jimmy", "Kim", "Howard", "Nacho", "Charles", "Lalo"]
turtle_color = [(255, 222, 0), (168, 218, 220), (16, 52, 166), (204, 85, 0), (90, 85, 147), (153, 0, 0)]
all_turtle = []
colormode(255)
for turtle_name in turtles:
    turtle = Turtle("turtle")
    turtle.color("black", turtle_color[turtles.index(turtle_name)])
    turtle.penup()
    turtle.goto(x, y)
    y += 50
    all_turtle.append(turtle)

if user_bet:
    game_one = True

while game_one:
    for turtle_name in all_turtle:
        if turtle_name.xcor() > 270:
            winning_turtle = turtles[all_turtle.index(turtle_name)]
            if winning_turtle ==user_bet:
                print(f"Spot on!! {winning_turtle} Wins!!")
            else:
                print(f"Sad!! {winning_turtle} won over your bet.")
            game_one = False
        rand_distance = randint(0,10)
        turtle_name.fd(rand_distance)

screen.exitonclick()