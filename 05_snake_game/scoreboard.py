from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.color("white")
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}", False, align="center", font=("Arial", 16, "normal"))


    def get_score(self):
        self.clear()
        self.score += 1
        self.print_score()


    def print_gameover(self):
        self.setpos(0, 0)
        self.write(f"Game over", False, align="center", font=("Arial", 16, "normal"))
