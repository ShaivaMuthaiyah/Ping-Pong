from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time



# initialise objects
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

#initialise players
paddle = Paddle((350,0),"light sky blue")
second_paddle = Paddle((-350, 0), "yellow")
ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle.paddle_up, "Up")
screen.onkey(paddle.paddle_down, "Down")
screen.onkey(second_paddle.paddle_up, "w")
screen.onkey(second_paddle.paddle_down, "s")


pong_game = True

while pong_game:

    time.sleep(0.1)
    screen.update()
    ball.movement()

    if ball.ycor() > 270 or ball.ycor() < -280 :
        ball.bounce()

    if ball.distance(paddle) < 40 and ball.xcor() > 305 :
        ball.increase_speed()
        ball.bounceback()

    if ball.distance(second_paddle) < 40 and ball.xcor() < -305 :
        ball.increase_speed()
        ball.bounceback()

    #Right side player miss

    if ball.xcor() > 380 :
        scoreboard.left_update_score()
        ball.reset_speed()
        ball.reset_position()


    #Left side player miss

    if ball.xcor() < -380 :
        scoreboard.right_update_score()
        ball.reset_speed()
        ball.reset_position()





screen.exitonclick()