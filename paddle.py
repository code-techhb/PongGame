from turtle import Turtle

# constants
STRETCH_WIDTH = 5
STRETCH_LENGTH = 1
Y_INCREMENT = 20


class Paddle(Turtle):
    # create a class that inherits from the turtle class
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("pink")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + Y_INCREMENT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - Y_INCREMENT
        self.goto(self.xcor(), new_y)
