import pyglet, inspect, importlib.util
from pyglet.gl import glEnable, glShadeModel, GL_SMOOTH, GL_TEXTURE_2D
from .globals import Globals
from .core import WindowManager
from .classes import *
from .functions import *

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

        try:
            self.setup = sketch.setup
        except:
            raise SystemExit("found no setup function! p5.py failed to start.")
        try:
            self.draw = sketch.draw
        except:
            raise SystemExit("could not find draw function, p5.py failed to start.")

        # start p5py
        self.start()

    def start(self):
        # run setup from sketch
        self.setup()

        glEnable(GL_TEXTURE_2D)  # enable textures
        glShadeModel(GL_SMOOTH)  # smooth shading of polygons

        event_loop = pyglet.app.EventLoop()
            
        def update(dt):
            self.draw()
            if not Globals.RUNNING:
                event_loop.exit()
        pyglet.clock.set_fps_limit(1/Globals.FPS)
        pyglet.clock.schedule_interval(update, 1/Globals.FPS)
        event_loop.run()


        # while Globals.RUNNING:
        #     dt = pyglet.clock.tick()
        #     pyglet.clock.set_fps_limit(30)

        #     # clear all windows
        #     for window in Globals.WINDOWMANAGER.windows:
        #         # draw background
        #         pyglet.gl.glClearColor(*window.drawsettings.backgroundcolor.get())
        #         window.window.clear()

        #     # call draw from sketch
        #     self.draw()

        #     # update all windows
        #     for window in Globals.WINDOWMANAGER.windows:
        #         # draw the batch class
        #         window.window.dispatch_events()
        #         window.window.dispatch_event('on_draw')
        #         window.window.flip()

init = Init()