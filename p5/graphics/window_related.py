from .color import Color
from .colors import Colors
from ..globals import Globals

def background(*args, **kwargs):
    for i in args:
        if type(i) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = i
            return
    for key, value in kwargs.items():
        if type(value) == Color:
            Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = value
            return
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.backgroundcolor = Color(*args, **kwargs)

    Globals.WINDOWMANAGER.selectedwindow.cls()

def clear():
    Globals.WINDOWMANAGER.selectedwindow.cls()

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
    set_minimum_size(x, y)

def draw_fps():
    Globals.WINDOWMANAGER.selectedwindow.draw_fps = not Globals.WINDOWMANAGER.selectedwindow.draw_fps

def font(name):
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.font.type = name

def fontsize(val:int):
    Globals.WINDOWMANAGER.selectedwindow.drawsettings.font.size = val

def loop():
    Globals.LOOP = True

def noloop():
    Globals.LOOP = False