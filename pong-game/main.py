from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
window=Screen()
window.bgcolor('black')
window.setup(width=800,height=600)
window.title("Pong")
window.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
score_board=ScoreBoard()

window.listen()
window.onkey(r_paddle.go_up,"Up")
window.onkey(r_paddle.go_down,"Down")
window.onkey(l_paddle.go_up,"w")
window.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.move()

    #Detect collision with wall.
    if ball.ycor()>275 or ball.ycor()<-275:
        ball.bounce_y()

    #Detect collision with the paddle.
    if 330 < ball.xcor() < 345 and abs(ball.ycor() - r_paddle.ycor()) < 50 and ball.x_move > 0:
        ball.bounce_x()

    if -345 < ball.xcor() < -330 and abs(ball.ycor() - l_paddle.ycor()) < 50 and ball.x_move < 0:
        ball.bounce_x()


    #Detect missed.
    if ball.xcor()> 380:
        score_board.l_point()
        ball.reset_position()

    if ball.xcor()<- 380:
        ball.reset_position()
        score_board.r_point()





window.exitonclick()