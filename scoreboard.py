
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def Update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 88, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 88, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.Update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.Update_score()
