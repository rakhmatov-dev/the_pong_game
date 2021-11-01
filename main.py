# TODO 1. Create the screen | DONE
# TODO 2. Create and move a paddle | DONE
# TODO 3. Create another paddle | DONE
# TODO 4. Create the ball and make it move | DONE
# TODO 5. Detect collision with wall and bounce | DONE
# TODO 6. Detect collision with paddle / DONE
# TODO 7. Detect when paddle misses
# TODO 8. Keep score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import PongBall
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = PongBall()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)

game_is_on = True
x_cor = 0
y_cor = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 330)
            or (ball.distance(left_paddle) < 50 and ball.xcor() < -330)):
        ball.bounce_x()

    # Detect when paddle misses the ball
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball = PongBall()

screen.exitonclick()