# 100 DAYS OF CODE USING PYTHON
# INSTRUCTOR: ANGELA YU
# Project 22 : Pong Game
# BY HOULAYMATOU B. | @code_techhb
# January 8, 2024

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from dashedline import Dash
import time

# objects
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title(titlestring="Welcome to the Pong Game")

# turn off the animation at the beginning
my_screen.tracer(0)

# game elements creation
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
line = Dash()

my_screen.listen()
# right paddle move
my_screen.onkey(fun=paddle_right.go_up, key="Up")
my_screen.onkey(fun=paddle_right.go_down, key="Down")
# left paddle move
my_screen.onkey(fun=paddle_left.go_up, key="e")
my_screen.onkey(fun=paddle_left.go_down, key="d")

game_on = True
while game_on:
    time.sleep(ball.increase_speed)
    my_screen.update()
    ball.refresh_ball_position()

    # detect if the ball has collided with the top/bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        # the ball should bounce back along the vertical
        ball.bounce_y()

    # detect collision with the paddles and make it bounce along the x axis
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if the ball is out the bounds of the screen: meaning right paddle has missed the ball
    if ball.xcor() > 380:
        # right paddle misses
        ball.reset_position()
        score.left_score()

    if ball.xcor() < -380:
        # left paddle misses
        ball.reset_position()
        score.right_score()

my_screen.exitonclick()
