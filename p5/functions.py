import pyglet
from .globals import Globals
from .classes import Color
from p5.classes import Vector

adjust_x, adjust_y = 0, 0
rotation = 0


def _get_coords(x, y):
    global adjust_x, adjust_y, rotation
    v = Vector(x, y)
    v.rotate('z', rotation)
    return v.x + adjust_x, v.y + adjust_y


def CreateVector(*args, **kwargs):
    return Vector(*args, **kwargs)


# def rect(x1,y1,x2,y2):
#
def point(x, y):
    Globals.WINDOWMANAGER.selectedwindow.batch.add(1, pyglet.gl.GL_POINTS, None,
                                                   ('v2i', _get_coords(x, y)),
                                                   ('c4f',
                                                    Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                        True))
                                                   )


# Shapes
def rect(x, y, w, h):
    line_color = Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokecolor.get()
    points = _get_coords(x, y) + _get_coords(x + w, y) + _get_coords(x + w, y + h) + _get_coords(x, y + h)
    Globals.WINDOWMANAGER.selectedwindow.batch.add(4, pyglet.gl.GL_QUADS, None,
                                                   ('v2f', points),
                                                   ('c4f',
                                                    4 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                        True))
                                                   )


def triangle(x1, y1, x2, y2, x3, y3):
    line_color = Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokecolor.get()
    points = _get_coords(x1, y1) + _get_coords(x2, y2) + _get_coords(x3, y3)
    Globals.WINDOWMANAGER.selectedwindow.batch.add(3, pyglet.gl.GL_TRIANGLES, None,
                                                   ('v2f', points),
                                                   ('c4f',
                                                    3 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                        True)))


# Transformations
def translate(x, y):
    global adjust_y, adjust_x
    adjust_x = x
    adjust_y = y

def rotate(rad):
    global rotation
    rotation = rad


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
    Globals.WINDOWMANAGER.selectedwindow.clear()
    Globals.WINDOWMANAGER.selectedwindow.batch.clear()
