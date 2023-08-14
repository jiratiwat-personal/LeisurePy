from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
ninjas = []
colorlist = ["red", "blue", "green", "black", "purple", "orange"]
dy = 400/7
for i in range(6):
    ninjas.append(Turtle(shape="turtle"))
    ninjas[i].color(colorlist[i])
    ninjas[i].penup()
    ninjas[i].goto(x=-230, y=200-dy*(i+1))
user_bet = (screen.textinput(title="Bet", prompt="Which ninja's color you bet? ")).lower()


goal = False
while not goal:
    for ninja in ninjas:
        ninja.forward(random.randint(0, 10))
        if ninja.pos()[0] >= 230:
            goal = True
            break


print(f"## {ninja.pencolor()} got to the finish line ##")
if ninja.pencolor() == user_bet:
    print("you win!")
else:
    print("you lose!")

screen.listen()
screen.exitonclick()
