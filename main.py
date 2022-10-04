from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
# Player
# Screen
# ball
# Scoreboard
#
# TODO- 1 Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Create and move a paddle
paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
ball = Ball()
player_score = Scoreboard()


screen.listen()
screen.onkey(fun=paddle_r.go_up, key='Up')
screen.onkey(fun=paddle_r.go_down, key='Down')
screen.onkey(fun=paddle_l.go_up, key='w')
screen.onkey(fun=paddle_l.go_down, key='s')

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 340 or ball.distance(paddle_l) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        player_score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        player_score.r_point()


# Create another paddle
# Create the ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score

screen.exitonclick()
