import pyglet,inspect,importlib.util
from .globals import *
from .core.program_loop import loop
from .screen.window import *
from .math import *


f = inspect.getouterframes(inspect.currentframe())[-1][1]
print(f)

# import sketch (from absolute path)
spec = importlib.util.spec_from_file_location("", f)
sketch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sketch)
Globals.FILE = sketch

eventloop = pyglet.app.EventLoop()
programloop = loop(eventloop)

pyglet.clock.set_fps_limit(Globals.FPS)
pyglet.clock.schedule_interval(programloop.update, 1 / Globals.FPS)
eventloop.run()















