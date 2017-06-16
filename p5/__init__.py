import pyglet, inspect, importlib.util
from pyglet.gl import glEnable, glShadeModel, GL_SMOOTH, GL_TEXTURE_2D
from .globals import *
from .core import WindowManager
from .classes import _CreateWindow as cw
from .classes import *
from .functions import *
from .math import *

from time import sleep


class Init:
    def __init__(self, setup=None, preload=None, draw=None):
        # list functions from main file to be called
        f = inspect.getouterframes(inspect.currentframe())[-1][1]
        Globals.FILE = f
        print(f)

        # import sketch (from absolute path)
        spec = importlib.util.spec_from_file_location("", Globals.FILE)
        sketch = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sketch)
        global KeyTyped, KeyPressed, KeyReleased,MousePressed,MouseDragged
        try:
            self.setup = sketch.setup
        except:
            raise SystemExit("found no setup function! p5.py failed to start.")
        try:
            self.draw = sketch.draw
        except:
            raise SystemExit("could not find draw function, p5.py failed to start.")
        try:
            self.KeyPressed = KeyPressed = sketch.KeyPressed
        except:
            print("No keyPressed")
            self.KeyPressed = KeyPressed = lambda: 0
        try:
            self.KeyReleased = KeyReleased = sketch.KeyReleased
        except:
            print("No keyReleased")
            self.KeyReleased = KeyReleased = lambda: 0
        try:
            self.KeyTyped = KeyTyped = sketch.KeyTyped
        except:
            print("No keyTyped")
            self.KeyTyped = KeyTyped = lambda: 0
        try:
            self.MouseDragged = MouseDragged
        except:
            print("No keyTyped")
            self.MouseDragged = MouseDragged = lambda: 0
        try:
            self.MousePressed = MousePressed
        except:
            print("No keyTyped")
            self.MousePressed = MousePressed = lambda: 0


        # start p5py
        self.start()

    def start(self):
        # run setup from sketch
        self.setup()

        glShadeModel(GL_SMOOTH)  # smooth shading of polygons

        event_loop = pyglet.app.EventLoop()

        def update(dt):
            for i in Globals.WINDOWMANAGER.windows:
                i.drawsettings.reset()

            if Globals.LOOP:
                self.draw()
            if not Globals.RUNNING:
                event_loop.exit()

        pyglet.clock.set_fps_limit(Globals.FPS)
        pyglet.clock.schedule_interval(update, 1 / Globals.FPS)
        event_loop.run()

def redraw():
    init.draw()

def _CreateWindow(*args, **kwargs):
    global KeyPressed, KeyTyped, KeyReleased,MouseDragged,MousePressed
    window = cw(*args,**kwargs, keypressed=KeyPressed, keytyped=KeyTyped, keyreleased=KeyReleased,mousedragged=MouseDragged,mousepressed=MousePressed)
    run = True
    return window


CreateWindow = _CreateWindow
init = Init()
