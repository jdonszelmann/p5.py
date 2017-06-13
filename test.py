from p5 import *
from random import randint


def setup():
    CreateWindow(640, 480)
    background(name="white")


def draw():
    fill(name="red")
    translate(100, 100)
    rotate(HALF_PI/2)
    rect(0, 0, 50, 50)

def KeyPressed():
	print(key)