import colorsys
from tkinter import N
import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(100)
s.bgcolor("black")
t.pensize(2)
c = ['white','fuchsia','yellow','blueviolet','green','lime','gold','red']
for i in range(360):
    for k in range(8):
        for l in range(2):
            t.pensize(2)
            t.circle(80+i*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(c[i%6])
turtle.done()