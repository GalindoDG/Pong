from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.listen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 55 and ball.xcor() > 320 or ball.distance(left_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 420:
        ball.new_ball()
        scoreboard.l_point()

    if ball.xcor() < -420:
        ball.new_ball()
        scoreboard.r_point()

screen.exitonclick()
