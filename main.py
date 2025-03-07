import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pin Pong Game")
screen.listen()
ball = Ball()
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0 ))

screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")

screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #detect the collision with wall
    if  ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()


    #detect the collision with paddles
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()

     #detect if the ball goes out of bounds at the edge of screen.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()




screen.exitonclick()