#Imports and setup
import turtle
import random
import math
turtle.tracer(False)

#Globals
artist = turtle.Turtle()
with open("turtcolors.txt", "r") as colors:
    colors = sorted(list({color for color in colors.read().split("\n")}),key=str.lower)

#Helpers
def makeTurt(name):
    name = turtle.Turtle()

def centerTurt(turt):
    turt.penup()
    turt.goto(0,0)
    turt.setheading(0)
    turt.pendown()

def drawSquare(turt: str = turtle.Turtle(), size: int = 10, horizOffset: int = 0, vertOffset: int = 0):
    turt.penup()
    turt.goto(-(size / 2) + horizOffset,(size / 2) + vertOffset)
    turt.pendown()
    for i in range(4):
        turt.fd(size)
        turt.rt(90)

def drawTriangle(turt = turtle.Turtle(), size: int = 10, horizOffset: int = 0, vertOffset: int = 0):
    turt.penup()
    turt.lt(90)
    turt.goto(horizOffset, size / math.sqrt(3) + vertOffset)
    turt.rt(150)
    turt.pendown()
    for i in range(3):
        turt.fd(size)
        turt.rt(120)

def drawHexagon(turt = turtle.Turtle(), size: int = 10, horizOffset: int = 0, vertOffset: int = 0):
    turt.penup()
    turt.goto(horizOffset - (size / 4), ((size * math.sqrt(3)) / 4) + vertOffset)
    turt.pendown()
    for i in range(6):
        turt.fd(size / 2)
        turt.rt(60)

def drawOctagon(turt = turtle.Turtle(), size: int = 10, horizOffset: int = 0, vertOffset: int = 0):
    turt.penup()
    turt.goto(horizOffset - (size / (3 * math.sqrt(2))), (size / 2) + vertOffset)
    turt.pendown()
    for i in range(8):
        turt.fd(size / (3 * math.sqrt(2)))
        turt.rt(45)

def drawSpiral(turt,size):
    if size <= 10:
        for i in range(2):
            turt.fd(size)
            turt.rt(90)
    else:
        for i in range(2):
            turt.fd(size)
            turt.rt(90)
        drawSpiral(turt,size - 10)

def drawShape(turt = turtle.Turtle(),
              sides: int = 3,
              sideLen: int = 100,
              horizOffset: int = 0,
              vertOffset: int = 0, 
              hideTurt: bool = False,
              centerTurt: bool = False,
              initHeading: int = 0,
              color: str = "black",
              fill: bool = False,
              turtSpeed: int = 0):
    #Set the speed of the turtle
    turt.speed(turtSpeed)
    #Check if the number of sides is valid
    if sides < 3:
        raise ValueError("Number of sides must be greater than or equal to 3")
    #Colors
    turt.color(color)
    if fill:
        turt.fillcolor(color)
    else:
        turt.fillcolor("white")
    #Check if the turtle is hidden
    if hideTurt == True:
        turt.hideturtle()
    #Position the turtle
    if centerTurt:
        turt.goto(horizOffset,vertOffset)#TODO Center the turtle
    else:
        turt.goto(horizOffset,vertOffset)
    turt.setheading(initHeading)
    #Draw the shape
    turt.begin_fill()
    for i in range(sides):
        turt.fd(sideLen)
        turt.rt(360 / sides)
    turt.end_fill()

def getSideLen(diameter: int = 100,
               sides: int = 3):
    #Finding important numbers from sides and diameter
    return diameter / sides #TODO Figure out <strong>THE MATH</strong>

#Main program
#TODO: test cases
#drawShape(artist, 3, getSideLen(200, 3))
#drawShape(artist, 4, 200)
for sideNum in range(471)[::-1]:
    #drawShape(artist, sideNum + 3, 50, color=random.choice(colors), fill=True, turtSpeed=0)
    drawShape(artist, sideNum + 3, 50, color=colors[sideNum], fill=True, turtSpeed=0, vertOffset=500, hideTurt=True)

artist.hideturtle()

#Window setup
turtle.update()
window = turtle.Screen()
window.exitonclick()