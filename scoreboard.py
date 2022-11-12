from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.color("light sky blue")
        self.write(f"Right:{self.right_score}", align="center", font=("Courier", 24, "bold"))
        self.color("yellow")
        self.goto(0, -280)
        self.write(f"Left:{self.left_score}", align="center", font=("Courier", 24, "bold"))


    def right_update_score(self):
        self.right_score += 1
        self.update_scoreboard()


    def left_update_score(self):
        self.left_score += 1
        self.update_scoreboard()

