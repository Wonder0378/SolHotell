"""
Created by: Samuel Hellqvist and Marcus Hedquist
Date: 09-03-2022
Info:

file that draws a turtle canvas
this will be used in the hotell project

"""
import turtle
from turtle import *


#preperation
hideturtle()
width(7)
speed(10)
bgcolor("#003f7d")
pencolor("#ff8e00")
up()
backward(250)
left(90)
forward(100)
left(180)

#H
down()
forward(150)
left(180)
forward(75)
right(90)
forward(75)
left(90)
forward(75)
left(180)
forward(150)

#move
up()
left(90)
forward(20)
left(90)
forward(37.5)
right(90)
down()

#e
forward(75)
left(90)
forward(37.5)
left(90)
forward(75)
left(90)
forward(75)
left(90)
forward(75)

#move
up()
forward(20)
left(90)
forward(75)
left(180)
down()

#j
forward(150)
right(90)
forward(37.5)
right(90)
forward(20)
up()
forward(160)
right(90)
forward(37.5)
right(90)
down()
forward(10)

#move
up()
forward(100)
left(90)
forward(95)
left(90)
down()

#d
forward(150)
left(180)
forward(75)
right(90)
forward(75)
left(90)
forward(75)
left(90)
forward(75)

#move
up()
forward(95)
left(90)
down()

#å
forward(75)
left(90)
forward(75)
left(90)
forward(75)
left(90)
forward(100)
up()
left(90)
forward(100)
left(90)
forward(45)
down()
forward(25)
right(90)
forward(10)
right(90)
forward(25)
right(90)
forward(10)

#move
up()
left(90)
forward(45)
right(90)
forward(120)
right(90)
down()

#--------
forward(200)
up()
forward(30)
down()

forward(180)
right(90)

#move
up()
left(180)
forward(50)
left(90)
forward(210)


#write välkommen åter
turtle.color('#ff8e00')
style = ('Brush Script MT', 30, 'italic')
turtle.write('Välkommen åter!', font=style)


#move
left(90)
forward(270)
left(90)
forward(260)

#write sammys solhotell 
style = ('Arial', 35)
turtle.write('☀ SAMMYS SOLHOTELL ☀', font=style)
done()
