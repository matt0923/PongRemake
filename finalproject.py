import turtle
#This is my Intro to Computer Science Final Project, a recreation of the game Pong, but Christmas themed
win = turtle.Screen()
win.title("Intro to Comp Sci Final Project, Christmas themed")
win.bgcolor("dark green")
win.setup(width=800, height=600)
win.tracer(0)
#to keep track of score
score_a = 0
score_b = 0
# to make the Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)
# to make the Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)
# to make the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1
# To display the score at the top of the box
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("WASD Player: 0              Arrow Key Player: 0", align="center", font=("arial", 30, "normal"))
#Code to move the left paddle up
def left_paddle_up():
	y = left_paddle.ycor()
	y += 20
	left_paddle.sety(y)
#Code to move the left paddle down
def left_paddle_down():
	y = left_paddle.ycor()
	y -= 20
	left_paddle.sety(y)
#Code to move the right paddle up
def right_paddle_up():
	y = right_paddle.ycor()
	y += 20
	right_paddle.sety(y)
#Code to move the right paddle down
def right_paddle_down():
	y = right_paddle.ycor()
	y -= 20
	right_paddle.sety(y)
# Keyboard binding
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")
# To keep the game running until the window is closed
while True:
    win.update()	
	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
	# What to do if the ball goes past the paddles
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("WASD Player: {}             Arrow Key Player: {}".format(score_a, score_b), align="center", font=("arial", 30, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("WASD Player: {}             Arrow Key Player: {}".format(score_a, score_b), align="center", font=("arial", 30, "normal"))
    # How the game reacts if the user hits the ball with the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1