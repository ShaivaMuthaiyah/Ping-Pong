from turtle import Turtle

class Screen_Elements(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(25, 0.2)
        self.goto(0,0)
