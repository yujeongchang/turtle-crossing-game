from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-270, 250)
        self.clear()
        self.write(f"Level: {self.level}", align= "left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def gameover(self):
        self.goto(-65, 0)
        self.write("GAME OVER", font= FONT)


