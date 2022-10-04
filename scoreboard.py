from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score(self):
        self.r_score += 1
        self.update_scoreboard()