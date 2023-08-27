from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.save_file = "save.txt"
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.color("white")
        self.high_score = 0
        self.load_highscore()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score} High score : {self.high_score}", False, align="center", font=("Arial", 16, "normal"))


    def get_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.print_score()


    def print_gameover(self):
        self.setpos(0, 0)
        self.write(f"Game over", False, align="center", font=("Arial", 16, "normal"))


    def load_highscore(self):
        if os.path.exists(self.save_file):
            # if file exists then check if empty or not
            with open(self.save_file, mode="r") as file:
                contents = file.read()
                if contents.strip():
                    self.high_score = int(contents)
        else:
            # if file does not exist then create new file and write 0
            with open(self.save_file, mode="w") as file:
                file.write("0")

    def save_highscore(self):
        with open("save.txt", mode="w") as file:
            file.write(str(self.high_score))