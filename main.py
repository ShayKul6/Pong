import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

POSITION_LEFT_PADDLE = (-350, 0)
POSITION_RIGHT_PADDLE = (350, 0)

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # stops automatic updates

# Create Objects / Instances
left_paddle = Paddle(POSITION_LEFT_PADDLE)
right_paddle = Paddle(POSITION_RIGHT_PADDLE)
ball = Ball()
left_score = Scoreboard((-100, 200))
right_score = Scoreboard((100, 200))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

#   Detect ball collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #   Detect ball collision with a paddle and bounce
    if ((ball.xcor() > 320 and ball.distance(right_paddle) < 50) or
            (ball.xcor() <= -320 and ball.distance(left_paddle) < 50)):
        ball.bounce_x()
        # ball.velocity *= 0.9  # ball becomes faster

#   Detect when right paddle misses (add point to left score)
    if ball.xcor() > 380:
        ball.reset_position()
        left_score.increase_score()

#   Detect when left paddle misses (add point to right score)
    if ball.xcor() < -380:
        ball.reset_position()
        right_score.increase_score()

screen.exitonclick()