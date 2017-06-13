from p5 import *
from random import randint


def setup():
	CreateWindow(640,480)
	background(name="red")

def draw():
	fill(name="red")
	
	for i in range(0,100):
		point(i,10)