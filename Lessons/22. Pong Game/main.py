from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# New Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200,height=900) # width / 2 = 600, height / 2 = 450
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((550,0))
left_paddle = Paddle((-550,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")    


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collistion with wall
    if ball.ycor() > 430 or ball.ycor() < -430:
        ball.bounce_wall()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 520 or ball.distance(left_paddle) < 50 and ball.xcor() < -520:
        ball.bounce_paddle()

    if ball.xcor() > 600: 
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -600:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
