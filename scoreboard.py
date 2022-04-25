from turtle import  Turtle

ALIGNMENT = "center"
FONT = ("Courier", 72, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def l_score(self):
        self.left_score += 1
        self.update_score()

    def r_score(self):
        self.right_score += 1
        self.update_score()