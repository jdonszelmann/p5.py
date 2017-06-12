import pyglet
from .globals import Globals
from .classes import Color


def CreateVector(*args, **kwargs):
    from p5.classes import Vector
    return Vector(*args, **kwargs)


# def rect(x1,y1,x2,y2):
#
def point(x,y):
    Globals.WINDOWMANAGER.selectedwindow.batch.add(1, pyglet.gl.GL_POINTS,None,
		('v2i', (10, 15)),
		('c4b',Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get())
	)
	# windowmanager.selectedwindow.batch.add(2, pyglet.gl.GL_POINTS,
	# 										('v2i', (10, 15, 30, 35)),
	# 										('c3B',(0,1,0))
	# 										)


# drawing propertird such as basckround, fill, stroke etc.
def background(*args, **kwargs):
    from p5.classes import Color
    Globals.WINDOWMANAGER.selectedwindow.batch.clear()

    for i in args:
        if type(i) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = color
            return
    for key, value in kwargs.items():
        if type(value) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = value
            return
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = Color(*args, **kwargs)


def fill(*args, **kwargs):
    Globals.WINDOWMANAGER.selectedwindow.batch.clear()

    for i in args:
        if type(i) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor = color
            return
    for key, value in kwargs.items():
        if type(value) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor = value
            return
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor = Color(*args, **kwargs)


# screen commands
def clear():
    Globals.WINDOWMANAGER.selectedwindow.window.clear()
    Globals.WINDOWMANAGER.selectedwindow.batch.clear()
