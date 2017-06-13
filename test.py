from p5 import *
from random import randint


def setup():
	window2 = CreateWindow(640,480)
	window1 = CreateWindow(640,480).select()
	background(name="lightpink")

def draw():


	fill(name="red")
	
	point(randint(0,100),randint(0,100))