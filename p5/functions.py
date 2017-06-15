import pyglet, sys
from .globals import Globals
from .classes import Color
from p5.classes import Vector
from p5.core import *
from .color import Colors


def _get_coords(x, y, coord1, coord2):
    v = Vector(coord1, coord2)
    v -= Vector(x, y)
    v.rotate('z', Globals.WINDOWMANAGER.selectedwindow.drawsettings.rotate)
    v += Vector(x, y)
    v += Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate
    return v.x, v.y


def CreateVector(*args, **kwargs):
    return Vector(*args, **kwargs)


def point(x, y):
    Globals.WINDOWMANAGER.selectedwindow.batch.add(1, pyglet.gl.GL_POINTS, graphstyle("DAN",
                                                                                      Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2i', _get_coords(x, y)),
                                                   ('c4f',
                                                    Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                        True))
                                                   )


# Shapes
def rect(x, y, w, h):
    originalx, originaly = x, y
    if Globals.WINDOWMANAGER.selectedwindow.drawsettings.rectmode == "CORNER" or Globals.WINDOWMANAGER.selectedwindow.drawsettings.rectmode == None:
        pass
    if Globals.WINDOWMANAGER.selectedwindow.drawsettings.rectmode == "CORNERS":
        w = abs(x - w)
        h = abs(y - h)
    if Globals.WINDOWMANAGER.selectedwindow.drawsettings.rectmode == "CENTER":
        x -= w // 2
        y -= h // 2
    if Globals.WINDOWMANAGER.selectedwindow.drawsettings.rectmode == "RADIUS":
        x -= w
        y -= h
        w *= 2
        h *= 2

    points = _get_coords(originalx, originaly, x, y) + _get_coords(originalx, originaly, x + w, y) + _get_coords(
        originalx, originaly, x + w, y + h) + _get_coords(originalx, originaly, x, y + h)
    Globals.WINDOWMANAGER.selectedwindow.batch.add(4, pyglet.gl.GL_QUADS, graphstyle("DAN",
                                                                                     Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2f', points),
                                                   ('c4f',
                                                    4 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                        True))
                                                   )


def line(x1, y1, x2, y2):
    points = _get_coords(x1, y2, x1, y1) + _get_coords(x1, y2, x2, y2)
    Globals.WINDOWMANAGER.selectedwindow.batch.add(2, pyglet.gl.GL_LINES, graphstyle("DAN",
                                                                                     Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2f', points),
                                                   ('c4f',
                                                    2 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.stroke.get(
                                                        True))
                                                   )


def triangle(x1, y1, x2, y2, x3, y3):
    line_color = Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokecolor.get()
    points = _get_coords(x1, y2, x1, y1) + _get_coords(x1, y2, x2, y2) + _get_coords(x1, y2, x3, y3)
    Globals.WINDOWMANAGER.selectedwindow.batch.add(3, pyglet.gl.GL_TRIANGLES, graphstyle("DA",
                                                                                         Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2f', points),
                                                   ('c4f',
                                                    3 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                        True))
                                                   )


def ellipse(x, y, w, h):
    ACCURACY = 500
    global ellipse_drawing
    if Globals.WINDOWMANAGER.selectedwindow.drawsettings.ellipsemode == "CENTER":
        start = (x, y)
        r_cos = 0.5 * w
        r_sin = 0.5 * h
    elif Globals.WINDOWMANAGER.selectedwindow.drawsettings.ellipsemode == "RADIUS":
        start = (x, y)
        r_cos = w
        r_sin = h
    elif Globals.WINDOWMANAGER.selectedwindow.drawsettings.ellipsemode == "RADIUS":
        pass
    points = []
    for i in range(ACCURACY):
        points.append(_get_coords(x, y, start[0] + math.cos(i / ACCURACY * 2 * math.pi) * r_cos,
                                  start[1] + math.sin(i / ACCURACY * 2 * math.pi) * r_sin))
    points = [i for sub in points for i in sub]
    Globals.WINDOWMANAGER.selectedwindow.batch.add(len(points) // 2, pyglet.gl.GL_POLYGON, graphstyle("DA",
                                                                                                      Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2f', points),
                                                   ('c4f', len(
                                                       points) // 2 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                       True))
                                                   )


# def test():
#     class CustomGroup1(pyglet.graphics.Group):
#         def set_state(self):
#             pyglet.gl.glPointSize(10.0)
#             # disable blending 
#             pyglet.gl.glDisable(pyglet.gl.GL_BLEND)
#             # turn on anti-aliasing
#             pyglet.gl.glEnable(pyglet.gl.GL_POINT_SMOOTH)
#             # enable use of alpha function 
#             pyglet.gl.glEnable(pyglet.gl.GL_ALPHA_TEST) 
#             # alpha comparison 
#             pyglet.gl.glAlphaFunc(pyglet.gl.GL_GREATER, 0.5) 

#     class CustomGroup2(pyglet.graphics.Group):
#         def set_state(self):
#             pyglet.gl.glDisable(pyglet.gl.GL_POINT_SMOOTH) 
#             pyglet.gl.glLineWidth(10.0)


#         def unset_state(self):
#             pyglet.gl.glDisable(pyglet.gl.GL_ALPHA_TEST) 
#             pyglet.gl.glDisable(pyglet.gl.GL_POINT_SMOOTH)


#     Globals.WINDOWMANAGER.selectedwindow.batch.add(4, pyglet.gl.GL_POINTS,CustomGroup1(),
#                                                     ('v2f',(50,10,50,30,150,10,150,30)),
#                                                     ('c4f', 4 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(True))
#                                                     )
#     Globals.WINDOWMANAGER.selectedwindow.batch.add(8,pyglet.gl.GL_LINES,CustomGroup2(),
#                                                     ('v2f',(50,10, 50,30, 150,10, 150,30, 50,10, 150,10, 50,30, 150,30)),
#                                                     ('c4f', 8 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(True))
#                                                     ) 
#     Globals.WINDOWMANAGER.selectedwindow.batch.add(4,pyglet.gl.GL_QUADS,None,
#                                                     ('v2f',(50.0, 10.0,50,30, 150.0, 30.0,150,10)),
#                                                     ('c4f', 4 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(True))
#                                                     )

def translate(x, y, absolute=False):
    if absolute:
        if type(x) == Vector:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate = x
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate = Vector(x, y)
    else:
        if type(x) == Vector:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate += x
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate += Vector(x, y)


<<<<<<< HEAD
def rotate(rad,absolute=False):
    if Globals.ANGLEMODE == "DEGREES":
        rad = radians(rad)
=======
def rotate(rad, absolute=False):
>>>>>>> 1ddb3b291fd257beb69cde06737de963b1d7bd57
    if absolute:
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.rotate = rad
    else:
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.rotate += rad


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


def stroke(*args, **kwargs):
    for i in args:
        if type(i) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.stroke = i
            return
    for key, value in kwargs.items():
        if type(value) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.stroke = value
            return
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.stroke = Color(*args, **kwargs)


def strokeweight(weight: int = 1):
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight = weight


def clear():
    Globals.WINDOWMANAGER.selectedwindow.clear()
    Globals.WINDOWMANAGER.selectedwindow.batch.clear()


def colors():
    l = []
    for i in list(Colors.__dict__.keys()):
        if not i.startswith("_") and i is not "getname":
            l.append(i)
    return l


def stop():
    sys.exit()


def caption(caption):
    Globals.WINDOWMANAGER.selectedwindow.set_caption(caption)


def fullscreen():
    Globals.WINDOWMANAGER.selectedwindow.maximize()


def push():
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.push()


def pop():
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.pop()


def rectmode(mode):
    if mode.upper() not in ["CENTER", "RADIUS", "CORNER", "CORNERS"]:
        raise ValueError("rectmode can be: {}".format('"CENTER","RADIUS","CORNER","CORNERS"'))
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.rectmode = mode


def maxsize(x, y):
    Globals.WINDOWMANAGER.selectedwindow.set_maximum_size(x, y)


def minsize(x, y):
    Globals.WINDOWMANAGER.selectedwindow.set_minimum_size(x, y)
