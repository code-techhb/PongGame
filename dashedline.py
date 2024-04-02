from turtle import Turtle

class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.goto(x=0, y=-300)
        for _ in range(50):
            self.pencolor("pink")
            self.pensize(width=3)
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
