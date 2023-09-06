# Making Snake Class to make snake in the snake game

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position=position)

    def add_segment(self, position):
        a = Turtle(shape="square")
        self.segments.append(a)
        a.color("green")
        a.penup()
        a.goto(position)

    def extend(self):
        self.add_segment(position=self.segments[-1].position())
    
    def move(self):
        for a_num in range(len(self.segments) - 1, 0, -1 ):
            x = self.segments[a_num - 1].xcor()
            y = self.segments[a_num - 1].ycor()
            self.segments[a_num].goto(x,y)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.up = self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.down = self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.right = self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.left = self.head.setheading(LEFT)