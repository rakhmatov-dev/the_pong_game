from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
UP_RIGHT = 45
DOWN_RIGHT = 315
DOWN_LEFT = 225
UP_LEFT = 135


class PongBall(Turtle):
    def __init__(self):
        super(PongBall, self).__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1