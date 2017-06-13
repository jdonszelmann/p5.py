from p5 import *
from random import randint


def setup():
    CreateWindow(640, 480)
    background(name="white")
    global r
    r = 0

def draw():
    global r
    # print(r)
    fill(name="red")
    translate(100, 100)
    rotate(r)
    rect(0, 0, 50, 50)

def KeyPressed():
    global r
    r += 1
    print(r)