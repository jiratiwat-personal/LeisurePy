from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-280, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def levelup(self):
        self.level += 1
        self.update_score()

    def gameover(self):
        self.setpos(0, 0)
        self.write("Game over", font=FONT, align="center")

