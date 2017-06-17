from pyglet import graphics


class Batch():
    def __init__(self):
        self.batch = graphics.Batch()

    def draw(self):
        self.batch.draw()

    def add(self, *args, **kwargs):
        self.batch.add(*args, **kwargs)

    def clear(self):
        self.batch = graphics.Batch()