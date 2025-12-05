# Lyle Osburne 9-12-2025
# Lab week 3 - This code utilizes the turtle module to paint my initials in different colors

import turtle
from random import random

screen = turtle.Screen()
pen =turtle.Turtle()
pen.speed(1)




pen.color("red", "purple")
pen.begin_fill()
pen.pensize(10)
pen.forward(50)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(50)
pen.end_fill()
pen.up()
pen.forward(100)
pen.down()
pen.color("black", "purple")
pen.begin_fill()
pen.forward(100)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.up()
pen.forward(40)
pen.down()
pen.forward(40)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(40)
pen.right(90)
pen.up()
pen.forward(40)
pen.end_fill()


screen.mainloop()
