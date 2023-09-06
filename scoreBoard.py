from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        self.updateScore()
        self.hideturtle()

    def gameover(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.color("red")
        self.write(arg = "GAME OVER", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.write(arg = f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()