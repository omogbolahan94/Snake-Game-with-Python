from turtle import Turtle

with open('data.txt') as opened_data:
    result = int(opened_data.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = result
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Aria", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Aria", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open('data.txt', 'w') as data:
            data.write(f"{self.high_score}")
        self.update_scoreboard()

    def score_update(self):
        self.score += 1
        self.update_scoreboard()
