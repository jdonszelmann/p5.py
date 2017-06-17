from ..globals import *
from .sketch_interaction import sketch

class loop:
    def __init__(self,eventloop):
        self.sketch = sketch()
        self.eventloop = eventloop
        self.sketch.setup()

    def update(self,dt):
        self.sketch.draw()

        if not Globals.RUNNING:
            self.eventloop.exit()
