from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
        # self.y_move = self.y_move*-1
        # here the self.y_move will decrease the value when the ball reach the Y cordinate of 260 and 260 then that time
        # bounce will call and it will add the self.ycor+(the changed value of self.y_move to the negative)
        # that result in moving the ball in back direction

    def bounce_x(self):
        self.x_move *= -1

        # for moving the ball
        # detect the collision point
        # then rebound the ball back to the random direction 400 width and 300 length
