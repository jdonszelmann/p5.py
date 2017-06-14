from p5 import *
from random import randint
import math

def setup():
    CreateWindow(640, 480)
    background(name="white")
    caption("hey!")
    fullscreen()

c = colors()
i = 0

def draw():
    global i, c
    i += 0.1
    try:
        background(name=c[int(i)])
    except:
        stop()

def KeyPressed():
    pass