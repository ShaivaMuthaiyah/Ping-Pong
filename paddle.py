from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coords, color):
        super().__init__()

        self.speed("fastest")
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(5, 1)
        self.goto(coords)


    def paddle_up(self):
        new_ycord = self.ycor() + 20
        self.goto(self.xcor(), new_ycord)

    def paddle_down(self):
        new_ycord = self.ycor() - 20
        self.goto(self.xcor(), new_ycord)


