from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 24, "normal"



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.update_score()
        self.hideturtle()


    def saved_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}" f"  High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

