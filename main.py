# Making the legendary snake game

from snake import Snake
from turtle import Screen
from food import Food
from scoreBoard import Score
import time

is_game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game") 
screen.tracer(0)

s = Snake()
f = Food()
score_card = Score()

screen.listen()
screen.onkey(key="w", fun=s.up)
screen.onkey(key="s", fun=s.down)
screen.onkey(key="a", fun=s.left)
screen.onkey(key="d", fun=s.right)

while is_game_on:
    screen.update()
    time.sleep(0.1)
    s.move()

# Collision with Food

    if s.head.distance(f) < 15:
        f.Refresh() 
        s.extend()
        score_card.increaseScore()

# Collision with Wall
    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        score_card.gameover()
        is_game_on = False

# Collision with Snake Body
    for segment in s.segments[1:]:
        if s.head.distance(segment) < 10:
            score_card.gameover()
            is_game_on = False

screen.exitonclick()