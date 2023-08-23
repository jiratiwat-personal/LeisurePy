import game_object
from turtle import Screen
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
time_delay = 0.05
start_delay = 0.05
decrement_delay = 0.5

r_paddle = game_object.Paddle(350, 0)
r_scoreboard = game_object.Scoreboard(-100, 220)
l_paddle = game_object.Paddle(-350, 0)
l_scoreboard = game_object.Scoreboard(100, 220)
ball = game_object.Ball()
screen.update()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

on = True
while on:
    r_scoreboard.update_score()
    l_scoreboard.update_score()
    screen.update()
    ball.move()
    # check collide
    if r_paddle.distance(ball) < 50 and ball.xcor() > 330:
        ball.x_direction *= -1
        time_delay *= decrement_delay
    if l_paddle.distance(ball) < 50 and ball.xcor() < -330:
        ball.x_direction *= -1
        time_delay *= decrement_delay
    if ball.pos()[0] == 380:
        r_scoreboard.got_score()
        time_delay = start_delay
    if ball.pos()[0] == -380:
        l_scoreboard.got_score()
        time_delay = start_delay
    time.sleep(time_delay)

screen.exitonclick()
