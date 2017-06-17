
class sketch:
    def __init__(self):
        from ..globals import Globals
        self.sketch = Globals.FILE

    def draw(self):
        self.sketch.draw()

    def setup(self):
        self.sketch.setup()