import pyglet
from ..globals import *
from ..core import batch
from ..graphics import drawsettings

class _window(pyglet.window.Window):
    def __init__(self,width,height,resizable=True,caption="p5.py"):
        self.batch = batch.Batch()
        self.drawsettings = drawsettings.DrawSettings()

        super().__init__(width,height,resizable=resizable,caption=caption)
        Globals.WINDOWMANAGER.add(self)

        self.cls()

    def on_draw(self):
        self.batch.draw()
        self.batch.clear()

    def cls(self):
        pyglet.gl.glClearColor(*self.drawsettings.backgroundcolor.get(True))
        self.clear()

    def on_close(self):
        Globals.WINDOWMANAGER.remove(self)
        self.close()

def CreateWindow(*args,**kwargs):
    return _window(*args,**kwargs)