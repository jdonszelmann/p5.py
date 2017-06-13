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
    global y, x, z
    translate(300, 300)
    rotate(math.sin(x))
    rect(math.sin(y)*50, math.cos(x)*50, 50* (abs(math.cos(y)) + 0.5), 50* (abs(math.sin(x)) + 0.5))
    y += 0.1; x += 0.1; z += 0.03
    translate(100, math.cos(y)*40+100)
    rotate(math.sin(x)*0.5)
    fill(Color(abs(math.cos(z))*255, abs(math.sin(z))*255, abs(math.cos(z))*255))
    triangle(0,0,100, 0, 50, 50)


def KeyPressed():
    pass

