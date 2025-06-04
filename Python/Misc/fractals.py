import turtle
import math
import random
import time
turtle.tracer(False)

with open("code/Python/turtlecolors.txt", "r") as colors:
    colors = sorted(list({color for color in colors.read().split("\n")}),key=str.lower)

#nankani
def drawNankani(turt,depth,size,dist:int = 300):
    turt.speed(0)
    turt.pensize(5)
    #base case
    if depth == 1:
        turt.begin_fill()
        turt.rt(115)
        turt.fillcolor(random.choice(colors))
        turt.pencolor(random.choice(colors))
        turt.fd(dist * 2)
        turt.end_fill()
    else:
        turt.begin_fill()
        turt.fillcolor(random.choice(colors))
        turt.pencolor(random.choice(colors))
        turt.circle(-size)
        turt.end_fill()
        turt.rt(60)
        turt.penup()
        turt.fd(dist)
        turt.pendown()
        drawNankani(turt,depth-1,size / 1.55, dist / 1.5)
    turt.hideturtle()

#koch
def drawKoch(turt,levels,size):
    turt.speed(0)
    if levels == 1:
        turt.fd(size)
    else:
        drawKoch(turt,levels-1,size)
        turt.lt(60)
        drawKoch(turt,levels-1,size)
        turt.rt(120)
        drawKoch(turt,levels-1,size)
        turt.lt(60)
        drawKoch(turt,levels-1,size)

#koch snowflake
def drawKochSnowflake(turt,levels,size):
    for i in range(3):
        drawKoch(turt,levels,size)
        turt.rt(120)

turtie = turtle.Turtle()
drawNankani(turtie,10,100)

turtle.update()
window = turtle.Screen()
window.bgcolor(random.choice(colors))
window.exitonclick()