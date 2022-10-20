# Import libraries.
import turtle
from tkinter import messagebox

# Creating window and specify its details.
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)                                        # prevent the window from updating from its own and give me the power to control the speed of updating later.

# Rackect_1 object creation.
Racket1 = turtle.Turtle()                               # Creating the object.
Racket1.speed(0)                                        # specify the speed of the Racket to the fastest : 0.
Racket1.shape("square")                                 # Specify the shape.
Racket1.color("green")                                  # Specify the color.
Racket1.shapesize(stretch_wid=5, stretch_len=1)         # Changing the defualt size which is 20*20 pixels with some factor multiplying it.
Racket1.penup()                                         # To avoid leaving any trace behind it while moving.
Racket1.goto(-350, 0)                                   # Specify the location or the coordinates of the Racket1

# Rackect2 object creation.
Racket2 = turtle.Turtle()                               # Creating the object.
Racket2.speed(0)                                        # specify the speed of the Racket to the fastest : 0.
Racket2.shape("square")                                 # Specify the shape.
Racket2.color("red")                                    # Specify the color.
Racket2.shapesize(stretch_wid=5, stretch_len=1)         # Changing the defualt size which is 20*20 pixels with some factor multiplying it.
Racket2.penup()                                         # To avoid leaving any trace behind it while moving.
Racket2.goto(350, 0)                                    # Specify the location or the coordinates of the Racket1.

# Ball object creation.
ball = turtle.Turtle()                                  # Creating the object.
ball.speed(0)                                           # specify the speed of the Racket to the fastest : 0.
ball.shape("square")                                    # Specify the shape.
ball.color("white")                                     # Specify the color.
ball.penup()                                            # To avoid leaving any trace behind it while moving.
ball.goto(0, 0)                                         # Specify the location or the coordinates of the Racket1.
ball.dx = 0.25                                          # specify 2.5 pixel for each time the ball moves in the x-axis.
ball.dy = 0.25                                          # specify 2.5 pixel for each time the ball moves in the y-axis.

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24,"normal"))

# Functions of contol
def Racket1_up():
    y = Racket1.ycor()                                  # to get the coordinate in the y-coordinate on the screen.
    y += 20                                             # The increment of the movment value.
    Racket1.sety(y)                                     # Using the value we increment to make it the new 
    
def Racket1_down():
    y = Racket1.ycor()                                  # to get the coordinate in the y-coordinate on the screen.
    y -= 20                                             # The increment of the movment value.
    Racket1.sety(y)                                     # Using the value we increment to make it the new value

def Racket2_up():
    y = Racket2.ycor()                                  # to get the coordinate in the y-coordinate on the screen.
    y += 20                                             # The increment of the movment value.
    Racket2.sety(y)                                     # Using the value we increment to make it the new 
    
def Racket2_down():
    y = Racket2.ycor()                                  # to get the coordinate in the y-coordinate on the screen.
    y -= 20                                             # The increment of the movment value.
    Racket2.sety(y)                                     # Using the value we increment to make it the new value

# Keyboard bindings
window.listen()                                         # This function tell the device to wait for any key input might happen.
window.onkeypress(Racket1_up, "w")                      # Tells the device when the "w" key is used call this function. The "w" must be lower case.
window.onkeypress(Racket1_down, "s")                    # Tells the device when the "w" key is used call this function. The "s" must be lower case.
window.onkeypress(Racket2_up, "Up")                     # Tells the device when the "Up" key is used call this function.
window.onkeypress(Racket2_down, "Down")                 # Tells the device when the "Down" key is used call this function.

# Game loop which contains the continuous running of the game.
while(True):
    window.update()                                     # For updating the screen every time the loop runs.

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)                    # Changing the ball position while moving in x-axis
    ball.sety(ball.ycor() + ball.dy)                    # Changing the ball position while moving in y-axis

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24,"normal"))

    if Racket1.ycor() > 250:
        Racket1.goto(-350, 250)

    elif Racket1.ycor() < -250:
        Racket1.goto(-350, -250)

    elif Racket2.ycor() > 250:
        Racket2.goto(350, 250)

    elif Racket2.ycor() < -250:
        Racket2.goto(350, -250)
        
    # Ball rebound from The Rackets
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Racket2.ycor() + 40 and ball.ycor() > Racket2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Racket1.ycor() + 40 and ball.ycor() > Racket1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 

    if score1 == 15:
        messagebox.showinfo("Ping Pong","Player 1 Wins :)")
        break

    elif score2 == 15:
        messagebox.showinfo("Ping Pong","Player 2 Wins :)")
        break

quit()