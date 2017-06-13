from p5 import *
from random import randint
import math

def setup():
    CreateWindow(640, 480)
    background(name="white")
    global deg
    deg = 0

y, x, z = 0, 0, 1

def draw():
    clear()
    fill(name="red")
    global y, x
    translate(300, 300)
    rotate(math.sin(x))
    rect(math.sin(y)*50, math.cos(x)*50, 50, 50)
    y += 0.1; x += 0.1
    translate(100, math.cos(y)*20+100)
    rotate(math.sin(x))
    triangle(0,0,100, 0, 50, 50)


def KeyPressed():
    pass

