from p5 import *
from random import randint
import math

def setup():
    CreateWindow(640, 480)
    background(name="white")
    caption("hey!")
    fullscreen()

col = 0
x,y = 0,0
n = True

def draw():
    if n: clear()
    global col, x, y
    fill(math.cos(0.2*col)*255, math.sin(0.2*col)*255, math.tan(0.2*col)*255)
    translate(math.cos(x)*100+200+math.sin(y-0.2)*25, math.atan(y)*100 + 100 + math.sin(x)*50+math.cos(y+3)*50)
    rotate(math.cos(y)*TAU)
    ellipse(0, 0, abs(math.cos(y)*50)+20, abs(math.sin(x)*30)+20)
    x += 0.05; y += 0.05; col += 0.1

    strokeweight(1)
    line(0,0,100,100)
    rotate(col)
    rectmode("CENTER")
    fill(255)
    translate(200,200)
    rect(400,400,500,500)

    stroke(255)
    text("hi",100,100)

def KeyPressed():
    global n
    if n: n = False
    else: n = True