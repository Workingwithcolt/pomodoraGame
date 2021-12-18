import time
from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
ball = Ball()
r_pa = Paddle((350, 0))
l_pa = Paddle((-350, 0))
# here the paddle class that are used as blue print for making the particuler class
screen.listen()

sc = Scoreboard()
screen.onkey(r_pa.go_up, "Up")
screen.onkey(r_pa.go_down, "Down")
screen.onkey(l_pa.go_up, "w")
screen.onkey(l_pa.go_down, "s")

is_true = True
while is_true:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision of ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # needs to bounce
        # collision with r_paddle
    if ball.distance(r_pa) < 50 and ball.xcor() > 320 or ball.distance(l_pa) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 360:
        ball.goto(0, 0)
        sc.l_point()
    if ball.xcor() < -350:
        ball.goto(0, 0)
        sc.r_point()


screen.exitonclick()
