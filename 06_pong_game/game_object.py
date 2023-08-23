from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        # self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(x_pos, y_pos)

    def go_up(self):

        self.goto(self.pos()[0], self.pos()[1]+20)

    def go_down(self):
        self.goto(self.pos()[0], self.pos()[1]-20)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1)
        self.penup()
        self.x_direction = 5
        self.y_direction = 5

    def move(self):
        if self.pos()[0] < 380 and self.pos()[0] > -380:
            self.goto(self.pos()[0] + self.x_direction, self.pos()[1] + self.y_direction)
        else:
            self.resetPosition()
        if self.pos()[1] > 285 or self.pos()[1] < -285:
            self.y_direction *= -1

    def resetPosition(self):
        self.x_direction *= -1
        self.setpos(0, 0)


class Scoreboard(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.setpos(x_pos, y_pos)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def got_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", font=("Arial", 50, "normal"))



