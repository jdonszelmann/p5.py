from ..globals import *
from ..math.vector import Vector
from ..math.math import *
import pyglet
from .graphstyle import graphstyle


def _get_coords(x, y, coord1, coord2):
    v = Vector(coord1, coord2)
    v -= Vector(x, y)
    v.rotate('z', Globals.WINDOWMANAGER.selectedwindow.drawsettings.rotate)
    v += Vector(x, y)
    v += Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate
    return v.x, v.y

def CreateVector(*args, **kwargs):
    return Vector(*args, **kwargs)

def text(txt,x,y):
    pyglet.text.Label(  txt,
                        batch= Globals.WINDOWMANAGER.selectedwindow.batch.batch,
                        x=x,
                        y=y,
                        font_size = Globals.WINDOWMANAGER.selectedwindow.drawsettings.font.size,
                        font_name = Globals.WINDOWMANAGER.selectedwindow.drawsettings.font.type,
                        color = Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(),
                        anchor_x = "center",
                        anchor_y = "center"
                    )

def point(x, y):
    Globals.WINDOWMANAGER.selectedwindow.batch.add( 1, pyglet.gl.GL_POINTS, graphstyle("DAN",Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2f', _get_coords(x,y,x, y)),
                                                   ('c4f',Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(True))
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
        points.append(_get_coords(x, y, start[0] + cos(i / ACCURACY * 2 * PI) * r_cos,
                                  start[1] + sin(i / ACCURACY * 2 * PI) * r_sin))
    points = [i for sub in points for i in sub]
    Globals.WINDOWMANAGER.selectedwindow.batch.add(len(points) // 2, pyglet.gl.GL_POLYGON, graphstyle("DA",
                                                                                                      Globals.WINDOWMANAGER.selectedwindow.drawsettings.strokeweight),
                                                   ('v2f', points),
                                                   ('c4f', len(
                                                       points) // 2 * Globals.WINDOWMANAGER.selectedwindow.drawsettings.fillcolor.get(
                                                       True))
                                                   )


