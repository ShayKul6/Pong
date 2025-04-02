from turtle import Turtle

WIDTH = 5
LENGTH = 1
PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # create paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.goto(position)

    def go_up(self):
        x = self.xcor()
        y = self.ycor()
        if y < 240:  # collision with upper wall
            self.goto(x, y + PADDLE_MOVE_DISTANCE)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()
        if y > -240:  # collision with down wall
            self.goto(x, y - PADDLE_MOVE_DISTANCE)