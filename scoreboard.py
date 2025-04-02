from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 45, "normal")


class Scoreboard(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.position = x_position
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.position)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()