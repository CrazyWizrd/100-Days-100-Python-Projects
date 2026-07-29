import colorgram
from turtle import *
from random import *

# colors = colorgram.extract(r'''C:\Users\OJAS CHHABRA\Documents\100DayProject\Day18\image.jpg''' , 30)
# colors_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_rgb.append((r,g,b))

# print(colors_rgb)

color_list = [(8, 110, 166), (187, 18, 64), (1, 152, 132), (134, 132, 124), (237, 34, 6), (121, 173, 114), (125, 43, 113), (3, 170, 122), (243, 25, 170), (46, 52, 138), (242, 168, 215), (197, 119, 210), (8, 98, 85), (151, 197, 79), (8, 91, 104), (199, 111, 149), (140, 78, 223), (107, 128, 195)]
# removed some odd and dark colors and changed some

jim = Turtle()
colormode(255)
jim.hideturtle()

x = -225
y = -225
while x != 275 and y != 275:
    while x != 275:
        jim.teleport(x,y)
        jim.dot(20, choice(color_list))
        x += 50
    x = -225
    y += 50

Screen().exitonclick()
