# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:52:16 2022

@author: svedi
"""

import turtle


wn = turtle.Screen()
wn.title("Pong by Rasmus Svedin")
wn.bgcolor("black")
wn.setup(width=400, height=300)
wn.tracer(0)

#Left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-175, 0) 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#Right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(175, 0) 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.2
ball.dy = -0.2

#Counter
counter = turtle.Turtle()
counter.speed(0)
counter.color("white")
counter.penup()
counter.hideturtle()
counter.goto(0, 90)
counter.write("P1 score: 0 | P2 score: 0", align="center", font=("Courier", 12, "normal" ))

#Score
score_a = 0
score_b = 0

#movement of left paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
#movement of right paddle

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keybinding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "l")     
    

#Main

while True:
    wn.update()
    
    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border check
    if ball.ycor() > 145:
        #winsound.PlaySound("bounce.mid", winsound.SND_ASYNC)
        ball.sety(145)
        ball.dy *= -1
    
    if ball.ycor() < -145:
        #winsound.PlaySound("bounce.mid", winsound.SND_ASYNC)
        ball.sety(-145)
        ball.dy *= -1
        
    if ball.xcor() > 195:
       score_a +=1 
       counter.clear()
       counter.write("P1 score: {} | P2 score: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal" ))
       ball.goto(0, 0)
       ball.dx = -0.2
       
    if ball.xcor() < -195:
       score_b +=1
       counter.clear()
       counter.write("P1 score: {} | P2 score: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal" ))
       ball.goto(0, 0)
       ball.dx = 0.2
       
    if paddle_a.ycor() > 180:
        paddle_a. sety(-180)
        
    if paddle_a.ycor() < -180:
        paddle_a. sety(180)
        
    if paddle_b.ycor() > 180:
         paddle_b. sety(-180)
         
    if paddle_b.ycor() < -180:
         paddle_b. sety(180)
       
    #collision
    if ball.xcor() > 170 and ball.xcor() < 190 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40:
       ball.setx(170)
       #winsound.PlaySound("bounce.mid", winsound.SND_ASYNC)
       ball.dx *= -1.1
       
    if ball.xcor() < -170 and ball.xcor() > -190 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40:
       ball.setx(-170)
       #winsound.PlaySound("bounce.mid", winsound.SND_ASYNC)
       ball.dx *= -1.1
       
