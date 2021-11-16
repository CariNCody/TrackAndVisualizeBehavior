#Cody Garcia
import csv
from turtle import *
from csv import writer
import math
import glob
import os

#These variables can be changed to your liking.

#The number of rows in the grid.
rows = 7
#The number of columns in the grid.
columns = 21
#Width of the grid. Box size is size/columns.
size = 1175
#Should the program run automatically, True or False.
Automatic = False
#If the program is set to automatic, enter the regular expression that matches your files.
expression = "/Five_Minute/R_id*.txt"
#The only way to change the hight of the grid is by changing the number of rows.

path = os.getcwd()

#Requests file to edit.
if Automatic == False:
    file = input(str("Enter file name: "))
if Automatic == True:
    filename = glob.iglob(path+expression)


#Sets up window size and name.
setup(width=size*1.2, height=(size/(columns/rows))*1.4)
title("Cody's Heated Fishy Grid")

#Changes turtle shape to an actual turtle.
shape("turtle")
resizemode("user")
shapesize((size/columns)/38.45, (size/columns)/38.45, (size/columns)/12.5)
#Repositions turtle to the center of the screen.


#Creates a folder to save heap map files in.
patheps = path+"/Heat_Maps"
try:
    os.mkdir(patheps)
except OSError:
    print ("Creation of the directory %s failed" % patheps)
else:
    print ("Successfully created the directory %s " % patheps)

#Starts Drawing
penup()
hideturtle()

#Draws Grid
def grid():
    setpos(0,0)
    setheading(0)
    k = 0
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
    penup()

#Shifts mathematical grid by 0.5 or 1 depending on if it's coloumns/rows are even or odd.
add = 0.5
subtract = 0.5
if columns % 2 == 0:
    add = 1
if rows % 2 == 0:
    subtract = 1
xprev = 0
yprev = 0

#Sets direction of turtle based on where it's going.
def direction(x, y):
    if x - xprev >= 1 and y - yprev == 0:
        setheading(0)
    if x - xprev >= 1 and y - yprev <= -1:
        setheading(45)
    if x - xprev == 0 and y - yprev <= -1:
        setheading(90)
    if x - xprev <= -1 and y - yprev <= -1:
        setheading(135)
    if x - xprev <= -1 and y - yprev == 0:
        setheading(180)
    if x - xprev <= -1 and y - yprev >= 1:
        setheading(225)
    if x - xprev == 0 and y - yprev >= 1:
        setheading(270)
    if x - xprev >= 1 and y - yprev >= 1:
        setheading(315)


def gotoandprint(x, y):
    rad = 0
    penup()
    global xprev
    global yprev
    global green
    global blue
    #Moves turtle coordinates to the middle of the box.
    xo = ((size/columns)*x-(size*0.5+(size/columns)*0.5))*math.cos(rad)-(-(size/columns)*y+((size/(columns/rows))*0.5+(size/columns)*0.5))*math.sin(rad)
    yo = (((size/columns)*x-(size*0.5+(size/columns)*0.5)))*math.sin(rad)+(-(size/columns)*y+((size/(columns/rows))*0.5+(size/columns)*0.5))*math.cos(rad)
    if xprev == 0 and yprev == 0 and columns >= x > 0 and rows >= y > 0:
        xprev = x
        yprev = y
    if columns >= x > 0 and rows >= y > 0: # and abs(xprev - x) <= 1 and abs(yprev - y) <= 1 and abs(xprev - x) + abs(yprev - y) != 0:
        direction(x, y) #Sets turtles direction
        goto(xo, yo) #Turtle goes to coordinates.
        global green
        global blue
        #Fills out field with colors.
        head = heading()
        setheading(0)
        colormode(255)
        fillcolor((0, green, blue))
        penup()
        forward((size/columns)/2)
        right(90)
        begin_fill()
        forward((size/columns)/2)
        right(90)
        forward(size/columns)
        right(90)
        forward((size/columns))
        right(90)
        forward(size/columns)
        right(90)
        forward((size/columns)/2)
        end_fill()
        right(90)
        forward((size/columns)/2)
        right(180)
        
        setheading(head)
        xprev = x
        yprev = y


def runfile(file):
    print(file)
    global xcords
    global ycords
    global green
    global blue
    xcords = []
    ycords = []
    #Reads data from file.
    with open(file, newline='', encoding='utf-8-sig') as csvfile:
        readout = csv.reader(csvfile, delimiter=' ')
        for row in readout:
            coordinates = row[0].split(',')
            if coordinates[0] != "x":
                #print(coordinates)
                xcords.append(int(coordinates[0]))
                ycords.append(int(coordinates[1]))
    #Selects colors for fields.
    placeholder = 0
    while placeholder < len(xcords):
        if Automatic == False:
            update()
        green = 255
        blue = 255
        run = 0
        while run < placeholder:
            if xcords[placeholder] == xcords[run] and ycords[placeholder] == ycords[run]:
                if green > 0:
                    green = green - 32
                elif blue > 0:
                    blue = blue - 32
            run = run + 1
        if green < 0:
            green = 0
        if blue < 0:
            blue = 0
        #Colors fields in.
        gotoandprint(xcords[placeholder],ycords[placeholder])
        placeholder = placeholder+1
    #Draws grid over colored fields.
    grid()
    hideturtle()
    update()
    ts = getscreen()
    ts.getcanvas().postscript(file=patheps+"/"+file[-17:-4]+".eps")

#Runs program.
if Automatic == True:
    for file in filename:
        tracer(0,0)
        runfile(file)
        clearscreen()

#Runs program.
if Automatic == False:
    tracer(0,0)
    runfile(file)








