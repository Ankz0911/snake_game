from turtle import Turtle

FONT = ('Arial', 16, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.penup()
        self.score = 0
        self.write(f"Score is :{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN , font = FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score is :{self.score}", align=ALIGN , font = FONT)
