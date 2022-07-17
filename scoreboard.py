from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-280, 260)
        self.color("black")
        self.score = 0
        self.write(f"Level: {self.score+1}", align='left', font=FONT)

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.score + 1}", align='left', font=FONT)

    def get_score(self):
        self.score += 1
        self.update_score()

    def print_score(self):
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("Game Over", align="center", font=FONT)



