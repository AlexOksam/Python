import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pd.read_csv("50_states.csv")

counter = 0
frame = True

while frame:
    answer_state = screen.textinput(title=f"{counter}/50 States Correct", prompt="What's another state's name?").title()
    if len(data[data.state == answer_state]) == 1:
        x = float(data.x[data.state == answer_state])
        y = float(data.y[data.state == answer_state])
        t.goto(x, y)
        t.write(answer_state, align="center", font=("Arial", 12, "normal"))
        counter += 1
        
    else: continue
