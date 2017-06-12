import pyglet
from .globals import Globals


def CreateVector(*args, **kwargs):
    from p5.classes import Vector
    return Vector(*args, **kwargs)


# def rect(x1,y1,x2,y2):
# 	
def point(x, y):
    Globals.WINDOWMANAGER.selectedwindow.batch.add(2, pyglet.gl.GL_POINTS,
                                           ('v2i', (10, 15, 30, 35)),
                                           ('c3B', (0, 1, 0))
                                           )


# drawing propertird such as basckround, fill, stroke etc.
def background(*args, **kwargs):
    from p5.classes import color
    from p5.core import windowmanager
    windowmanager.selectedwindow.batch.clear()

    for i in args:
        if type(i) == color:
            windowmanager.selectedwindow.drawsettings.backgroundcolor = color
            return
    for key, value in kwargs.items():
        if type(value) == color:
            windowmanager.selectedwindow.drawsettings.backgroundcolor = value
            return
    windowmanager.selectedwindow.drawsettings.backgroundcolor = color(*args, **kwargs)


def fill(*args, **kwargs):
    from p5.classes import color
    from p5.core import windowmanager
    windowmanager.selectedwindow.batch.clear()

    for i in args:
        if type(i) == color:
            windowmanager.selectedwindow.drawsettings.fillcolor = color
            return
    for key, value in kwargs.items():
        if type(value) == color:
            windowmanager.selectedwindow.drawsettings.fillcolor = value
            return
    windowmanager.selectedwindow.drawsettings.fillcolor = color(*args, **kwargs)


# screen commands
def clear():
    from p5.core import windowmanager
    windowmanager.selectedwindow.window.clear()
    windowmanager.selectedwindow.batch.clear()
