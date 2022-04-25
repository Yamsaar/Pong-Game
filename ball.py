from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 4
        self.y_move = 4
        self.ball_spead = 0.1

    def move_ball(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.ball_spead *= 0.5

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.ball_spead = 0.1
        self.bounce_x()