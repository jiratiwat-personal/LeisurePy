from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, turtle_speed):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.move_speed = turtle_speed
        self.setpos(300, random.randint(-250, 250))

    def move(self):
        self.forward(self.move_speed)

    def set_speed(self, turtle_speed):
        self.move_speed = turtle_speed

