from .sketch_interaction import sketch

class Loop:
    def __init__(self,eventloop):
        from ..globals import Globals

        self.sketch = sketch()
        self.eventloop = eventloop
        self.sketch.setup()
        Globals.EVENT_LOOP = self

        global Globals
        from ..globals import Globals


    def update(self,dt):
        if Globals.LOOP:
            self.sketch.draw()

        if not Globals.RUNNING:
            self.eventloop.exit()
