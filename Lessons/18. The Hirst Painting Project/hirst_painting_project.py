from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
tim.speed(100)
screen = Screen()
screen.colormode(255)

colors = colorgram.extract('Screenshot_2.jpg', 20)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if b < 200:
        new_color = (r, g, b)
        rgb_colors.append(new_color)

tim.hideturtle()
tim.penup()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)

number_of_dods = 100

for dot_counts in range(1, number_of_dods + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
