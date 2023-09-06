from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("whitesmoke")
        self.Refresh()

    def Refresh(self):
        x_position = random.randint(-260, 260)
        y_position = random.randint(-260, 260)
        self.goto(x_position, y_position)