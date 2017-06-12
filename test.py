from p5 import *


def setup():
	CreateWindow(640,480)

def draw():
	background(name="white")

	for i in range(10,100):
		point(i,10)