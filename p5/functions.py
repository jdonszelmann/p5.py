import pyglet
from p5.core import *
from p5.classes import *


def CreateVector(*args,**kwargs):
	return Vector(*args,**kwargs)


# def rect(x1,y1,x2,y2):
# 	
def point():
	pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    ('v2i', (10, 15, 30, 35))
)