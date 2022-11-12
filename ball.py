from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10


    def movement(self):
        new_y_cords = self.ycor() + self.y_move
        new_x_cords = self.xcor() + self.x_move
        self.goto(new_x_cords,new_y_cords)

    def bounce(self):
        self.y_move *= -1

    def bounceback(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounceback()

    def increase_speed(self):
        self.x_move += 2
        self.y_move += 2

    def reset_speed(self):
        self.x_move = 10
        self.y_move = 10
