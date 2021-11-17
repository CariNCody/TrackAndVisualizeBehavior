#Cody Garcia's Fish Grid.
#Written by Cody Garcia.
#Released 16/11/2021
from turtle import *
from csv import writer
import math

#These variables can be changed to your liking.

#The number of rows in the grid.
rows = 7
#The number of columns in the grid.
columns = 21
#Width of the grid. Box size is size/columns.
size = 1179
#Rolls/tilts the entire grid in degrees to the left (negative values to the right).
roll = -0.8
#Defines how transparent the window will become. 0 transparent - 1 opaque.
transparency = 0.3
#Keep in mind that the boxes are always squares.
#The only way to change the hight of the grid is by changing the number of rows.

#Requests file to edit.
file = input(str("Enter file name: "))
#file = file + ".txt"
#Sets up window size and name.
setup(width=size*1.2, height=(size/(columns/rows))*1.4+(abs(roll)*10))
title("Cody's Fishy Grid")

#Draws grid.
k = 0
left(roll)
speed(-1)
penup()
backward(size*0.5)
left(90)
forward(size/((columns/rows)*2))
right(90)
pendown()
right(90)
forward(size/(columns/rows))
penup()
backward(size/(columns/rows))
left(90)
pendown()
while k < columns:
    forward(size/columns)
    right(90)
    forward(size/(columns/rows))
    penup()
    backward(size/(columns/rows))
    left(90)
    pendown()
    k = k+1
k = 0
penup()
right(90)
pendown()
while k < rows:
    forward(size/columns)
    right(90)
    forward(size)
    penup()
    backward(size)
    left(90)
    pendown()
    k = k+1
k = 1
backward(size/(columns/rows))
left(90)
backward(size)
while k <= columns:
    write(k, font=("Calibri", int(round(size/(columns*2), 0)), "normal"))
    penup()
    forward(size/columns)
    pendown()
    k = k+1
penup()
backward(size+size/(1.5*columns))
right(90)
forward(size/(columns*1.5))
k = 1
while k <= rows:
    write(k, font=("Calibri", int(round(size/(columns*2), 0)), "normal"))
    penup()
    forward(size/columns)
    pendown()
    k = k+1
#End of drawing.

#Changes turtle shape to an actual turtle.
shape("turtle")
resizemode("user")
shapesize((size/columns)/38.45, (size/columns)/38.45, (size/columns)/12.5)
#Repositions turtle to the center of the screen.
penup()
setpos(0,0)
right(180)
hideturtle()
#Defines how to write into a file.
def append_list_as_row(file, data): 
    with open(file, 'a+', newline='') as write_obj: #Opens file in append mode.
        csv_writer = writer(write_obj) #Creates a writer object from csv module.
        csv_writer.writerow(data) #Add contents of list as last row in the csv file.

#Shifts mathematical grid by 0.5 or 1 depending on if it's coloumns/rows are even or odd.
add = 0.5
subtract = 0.5
if columns % 2 == 0:
    add = 1
if rows % 2 == 0:
    subtract = 1
xprev = 0
yprev = 0
rad = roll/180*math.pi #Puts "roll" into radian.

#Sets direction of turtle cursor.
def direction(x, y):
    if x - xprev >= 1 and y - yprev == 0:
        setheading(0+roll)
    if x - xprev >= 1 and y - yprev <= -1:
        setheading(45+roll)
    if x - xprev == 0 and y - yprev <= -1:
        setheading(90+roll)
    if x - xprev <= -1 and y - yprev <= -1:
        setheading(135+roll)
    if x - xprev <= -1 and y - yprev == 0:
        setheading(180+roll)
    if x - xprev <= -1 and y - yprev >= 1:
        setheading(225+roll)
    if x - xprev == 0 and y - yprev >= 1:
        setheading(270+roll)
    if x - xprev >= 1 and y - yprev >= 1:
        setheading(315+roll)

def gotoandprint(xo, yo):
    #Makes variables universal. Variables can be used inside and outside this definition.
    global xprev
    global yprev
    xp = xo*math.cos(rad)+yo*math.sin(rad) #Calculates x coordinate in rotated system.
    yp = yo*math.cos(rad)-xo*math.sin(rad) #Calculates y coordinate in rotated system.
    x = int(xp/(size/columns)+(add+math.ceil(columns/2))) #Calculates x in grid.
    y = int(abs((yp/(size/columns)-(subtract+math.ceil(rows/2))))) #Calculates y in grid.
    #Moves cursor coordinates to the middle of the box.
    xo = ((size/columns)*x-(size*0.5+(size/columns)*0.5))*math.cos(rad)-(-(size/columns)*y+((size/(columns/rows))*0.5+(size/columns)*0.5))*math.sin(rad)
    yo = (((size/columns)*x-(size*0.5+(size/columns)*0.5)))*math.sin(rad)+(-(size/columns)*y+((size/(columns/rows))*0.5+(size/columns)*0.5))*math.cos(rad)
    #Lets user select where the turtle starts from.
    if xprev == 0 and yprev == 0 and columns >= x > 0 and rows >= y > 0:
        goto(xo, yo)
        print(x, y)
        data = [x, y]
        append_list_as_row(file, data) #Appends beginning coordinates to file.
        xprev = x
        yprev = y
        showturtle()
        #Saves and prints the box turtle moves to
    if columns >= x > 0 and rows >= y > 0 and abs(xprev - x) <= 1 and abs(yprev - y) <= 1 and abs(xprev - x) + abs(yprev - y) != 0:
        direction(x, y) #Sets turtles direction
        goto(xo, yo) #Turtle goes to cursor coordinates.
        print(x, y)
        data = [x, y]
        append_list_as_row(file, data) #Appends coordinates to file. Doesn't have to be same variables as in def.
        xprev = x
        yprev = y
        
def jump(xo, yo):
    counter = 0
    #Since xprev is universal, must use a new variable that is based off of xprev for this definiton.
    xpre = xprev
    ypre = yprev
    xp = xo*math.cos(rad)+yo*math.sin(rad) #Calculates x coordinate in rotated system.
    yp = yo*math.cos(rad)-xo*math.sin(rad) #Calculates y coordinate in rotated system.
    x = int(xp/(size/columns)+(add+math.ceil(columns/2))) #Calculates x in grid.
    y = int(abs((yp/(size/columns)-(subtract+math.ceil(rows/2))))) #Calculates y in grid.
    #Lets turtle run in a straight line while recoring coordinates.
    if y-yprev == 0 and abs(x-xprev) > 1 or x-xprev == 0 and abs(y-yprev) > 1 or abs(xpre - x) - abs(ypre - y) == 0 and abs(xpre - x) > 1 and abs(ypre - y) > 1:
        direction(x, y)
        while counter < abs(xpre - x) or counter < abs(ypre - y):
            if heading() % 90 != 0:
                forward(size/columns)
            else:
                forward(math.sqrt(2)*size/columns)
            gotoandprint(xcor(), ycor())
            counter = counter+1

#Excecution of gotoandprint in relation to cursor click.
onscreenclick(gotoandprint, 1) #1 = left click
onscreenclick(jump, 2) #2 = right click

#Alters window transparency.
turtle = getturtle()
root = (turtle
    ._screen
    .getcanvas()
    .winfo_toplevel())
root.attributes('-alpha', transparency)
