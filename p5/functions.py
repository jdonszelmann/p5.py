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
        ('v2i', (x,y)),
        ('c4f',Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(True))
    )


def rect(x, y, w, h):
    line_color = Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokecolor.get()
    fill_collor = Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get()
    points = (x,y,x+w, y,x+w, y+h,x, y+h)
    
    Globals.WINDOWMANAGER.selectedwindow.batch.add(4, pyglet.gl.GL_QUADS, None,
                                                   ('v2f', points),
                                                   ('c4f',4*Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(True))
                                                   )




# drawing propertird such as basckround, fill, stroke etc.
def background(*args, **kwargs):
    from p5.classes import Color
    Globals.WINDOWMANAGER.selectedwindow.batch.clear()

    for i in args:
        if type(i) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = i
            return
    for key, value in kwargs.items():
        if type(value) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = value
            return
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = Color(*args, **kwargs)


def fill(*args, **kwargs):
    for i in args:
        if type(i) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor = i
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
