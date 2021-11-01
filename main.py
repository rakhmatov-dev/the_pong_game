# TODO 1. Create the screen | DONE
# TODO 2. Create and move a paddle
# TODO 3. Create another paddle
# TODO 4. Create the ball and make it move
# TODO 5. Detect collision with wall and bounce
# TODO 6. Detect collision with paddle
# TODO 7. Detect when paddle misses
# TODO 8. Keep score

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(x=350, y=0)


def go_up():
    right_paddle.goto(x=right_paddle.xcor(), y=right_paddle.ycor() + 20)


def go_down():
    right_paddle.goto(x=right_paddle.xcor(), y=right_paddle.ycor() - 20)


screen.listen()
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()