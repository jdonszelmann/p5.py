from p5 import *
from random import randint
import math

def setup():
    CreateWindow(640, 480)
    background(name="white")
    caption("hey!")
    fullscreen()
    minsize(600,400)
    maxsize(1200,800)

r = 0

def draw():
    global r
    background()
    r += 0.01

    strokeweight(1)
    line(0,0,100,100)
    rotate(r)
    rectmode("CENTER")
    fill(255)
    translate(200,200)
    rect(400,400,500,500)

    stroke(255)
    text("hi",100,100)

def KeyPressed():
    pass