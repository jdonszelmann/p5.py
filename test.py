from p5 import *
from random import randint
import math

def setup():
    CreateWindow(640, 480)
    background(name="white")
    caption("hey!")
    fullscreen()

r = 0

def draw():
    global r
    background()
    r += 0.01
    rotate(r)
    rectmode("CORNERS")
    fill(255)
    translate(200,200)
    rect(400,400,500,500)

def KeyPressed():
    pass