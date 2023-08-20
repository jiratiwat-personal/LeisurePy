import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
size = 20
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake(5)
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

on = True
while on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.snakeHead.distance(food) < 15:
        food.refresh()
        snake.ate = True
        scoreboard.get_score()

    if snake.snakeHead.pos()[0] > 280 or snake.snakeHead.pos()[0] < -280 or snake.snakeHead.pos()[1] < -280 or snake.snakeHead.pos()[1] > 280:
        on = False
        scoreboard.print_gameover()

    if snake.eat_own_tail():
        on = False
        scoreboard.print_gameover()

screen.exitonclick()