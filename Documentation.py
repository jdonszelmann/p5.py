from p5 import *


def setup():
    global window
    window = CreateWindow(640, 480,resizable=False)
    caption("p5.py Reference!")
    background(51)


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