from turtle import  Turtle

class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.penup()
        self.goto(positions)
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 1)

    def move_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

