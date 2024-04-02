from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=250)
        self.write(arg=f"Score: {self.l_score}", align="center", font=("Courier", 32, "normal"))
        self.goto(x=100, y=250)
        self.write(arg=f"Score: {self.r_score}", align="center", font=("Courier", 32, "normal"))

    def left_score(self):
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.r_score += 1
        self.update_score()
