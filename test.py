from p5 import *


def setup():
    CreateWindow(640,480)
    caption("hey!")

def draw():
    stroke(255)
    strokeweight(200)
    line(0,0,100,100)