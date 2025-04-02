from turtle import Turtle

WIDTH = 1
LENGTH = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1  # Change 'x' direction
        self.velocity *= 0.9  # increases ball speed

    def bounce_y(self):
        self.y_move *= -1  # Change 'y' direction

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()