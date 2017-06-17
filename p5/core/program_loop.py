from .sketch_interaction import sketch

class Loop:
    def __init__(self,eventloop):
        self.sketch = sketch()
        self.eventloop = eventloop
        self.sketch.setup()

        global Globals
        from ..globals import Globals


    def update(self,dt):
        self.sketch.draw()

        if not Globals.RUNNING:
            self.eventloop.exit()
