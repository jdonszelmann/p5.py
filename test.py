from p5 import *
from random import randint


def setup():
	CreateWindow(640,480)
	background(name="lightpink")

def draw():


	fill(name="red")
	
	point(randint(0,100),randint(0,100))