from ..globals import Globals
from ..math.vector import Vector
from .color import Color

def rotate(rad, absolute=False):
    if absolute:
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.rotate = rad
    else:
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.rotate += rad


def translate(x, y, absolute=False):
    if absolute:
        if type(x) == Vector:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate = x
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate = Vector(x, y)
    else:
        if type(x) == Vector:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate += x
        Globals.WINDOWMANAGER.selectedwindow.drawsettings.translate += Vector(x, y)

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
