from p5 import *
from random import randint


def setup():
    CreateWindow(640, 480)
    background(name="white")


def draw():
    fill(name="red")
    point(randint(0, 50), randint(0, 50))
    rect(200, 200, 50, 50)

def KeyPressed():
	print(key)