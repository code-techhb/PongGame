from turtle import Turtle

# CONSTANCE'S
INITIAL_COORDINATES = (0, 0)
INCREMENT = 20


class Ball(Turtle):
    # make the ball class have the same properties as the turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("lightgreen")
        self.goto(INITIAL_COORDINATES)
        self.y_move = 10
        self.x_move = 10
        self.increase_speed = 0.1


    def refresh_ball_position(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """This function bounces the ball along the y-axis whenever the ball touched the wall."""
        self.y_move *= -1


    def bounce_x(self):
        """This function bounce the ball along the x-axis whenever it touches a paddle."""
        self.x_move *= -1
        self.increase_speed *= 0.9

    def reset_position(self):
        """This function reset the ball position whenever a player misses the ball."""
        self.goto(INITIAL_COORDINATES)
        # reset the speed whenever a player lost
        self.increase_speed = 0.1
        self.bounce_x()

