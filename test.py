from p5 import *
import math

def setup():
    global window
    window = CreateWindow(640, 480)
    caption("hey!")
    background(51)
    print(pymap(5,0,10,0,1))


x,y,w = 0,0,0

def draw():
    global x,y,w, window
    translate(0,window.width/2)
    x += 1
    y += noise(1,w)
    w += 0.1
    point(x,y)

def KeyPressed():
    background(name = random(colors()))