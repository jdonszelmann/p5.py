import pyglet
from pyglet.window import key as k
from ..core import batch
from ..graphics import drawsettings
from ..globals import *

class _window(pyglet.window.Window):
    def __init__(self,width,height,resizable=True,caption="p5.py"):
        self.batch = batch.Batch()
        self.drawsettings = drawsettings.DrawSettings()
        self.onscreen = None

        super().__init__(width,height,resizable=resizable,caption=caption)
        Globals.WINDOWMANAGER.add(self)

        self.cls()
        self.fps_display = pyglet.clock.ClockDisplay()

    def on_draw(self):
        self.batch.draw()
        self.batch.clear()

        #devoption - show fps
        if True:
            self.fps_display.draw()

    def resize(self,w,h):
        self.set_size(w,h)

    @property
    def size(self):
        return Vector(self.get_size())

    @property
    def width(self):
        return self.get_size()[0]

    @property
    def height(self):
        return self.get_size()[1]

    def on_mouse_leave(self,x, y):
        self.onscreen = False

    def on_mouse_enter(self,x, y):
        self.onscreen = True

    def select(self,select=False):
        Globals.WINDOWMANAGER.select(self)
        if select:
            self.switch_to()
            self.activate()

    @property
    def selected(self):
        if Globals.WINDOWMANAGER.selectedwindow == self:
            return True
        return False

    def on_mouse_motion(self,x, y, dx, dy):
        mousex.set(x)
        mousey.set(y)
        rmousex.set(dx)
        rmousey.set(dy)
        Globals.EVENT_LOOP.sketch.mousedragged()


    def on_mouse_press(self,x, y, button, modifiers):
        try:
            self.MousePressed()
        except AttributeError:
            pass

    def on_key_press(self, symbol, mods):
        try:
            if modifiers == 0:
                keycode.set(ord(k.symbol_string(symbol)))
            else:
                keycode.set(None)
        except TypeError:
            keycode.set(None)
        key.set(k.symbol_string(symbol).replace("_", ""))
        if modifiers != 0:
            modifiers.set(k.modifiers_string(mods).replace("|", ",").replace("MOD_", ""))
        else:
            modifiers.set(None)
        keyispressed.set(True)
        Globals.EVENT_LOOP.sketch.keypressed()

        if mods == 0:
            Globals.EVENT_LOOP.sketch.keytyped()

    def on_key_release(self, symbol, modifiers):
        Globals.EVENT_LOOP.sketch.keyreleased()

    def cls(self):
        pyglet.gl.glClearColor(*self.drawsettings.backgroundcolor.get(True))
        self.clear()

    def on_close(self):
        Globals.WINDOWMANAGER.remove(self)
        self.close()

def CreateWindow(*args,**kwargs):
    return _window(*args,**kwargs)