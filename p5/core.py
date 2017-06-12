from pyglet.gl import *


class WindowManager:
    def __init__(self):
        self.windows = []
        self.selectedwindow = None

    def new_window(self, parent, w, h, resizable):
        win = pyglet.window.Window(w, h, resizable=True)
        self.windows.append(parent)
        if len(self.windows) == 1:
            self.selectedwindow = parent
        return win

    def remove(self, window):
        self.windows.remove(window)
        window.window.close()
        if len(self.windows) == 0:
            Globals.RUNNING = False


class DrawSettings:
    def __init__(self):
        from p5.classes import color
        # color related properties
        self.strokecolor = color(255, 255, 255)
        self.backgroundcolor = color(255, 0, 255)
        self.fillcolor = color(255, 255, 255)
        # value related properties
        self.strokeweight = 1


class Batch():
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

    def draw(self):
        self.batch.draw()

    def add(self, *args, **kwargs):
        self.batch.add(*args, **kwargs)

    def clear(self):
        self.batch = pyglet.graphics.Batch()


"""
VectorSet class

collects Vectors in an array to form a set which can be manipulated all at once

for example:
	s = vectorset(Vector(0,0),Vector(5,5))
	s.translate() #translates both vectors

used in coordinate manipulation (coordinates are stored as vectors)
"""


class _vectorset:
    def __init__(self, vectors=[]):
        self.vectors = vectors

    def __getitem__(self, key):
        return self.vectors[key]

    def __setitem__(self, key, value):
        self.vectors[key] = value

    def scale(self, x=1, y=1, z=1):
        from p5.classes import CreateVector
        scale_vector = CreateVector(x, y, z)
        for elem in self.vectors:
            elem *= scale_vector

    def rotate(self, axis, val):
        for elem in self.vectors:
            elem.rotate(axis, val)

    def translate(self, vector):
        for i in self.vectors:
            i += vector

    def copy(self):
        return self.__class__(self.vectors)

    def __iter__(self):
        for i in self.vectors:
            yield i

    def __repr__(self):
        return 'VectorSet: {}'.format(self.vectors)

    def __str__(self):
        return 'VectorSet: {}'.format(self.vectors)

    def __len__(self):
        return len(self.vectors)

    def add(self, vector):
        if not vector in self.vectors:
            self.vectors.append(vector)

    def remove_duplicates(self):
        self.vectors = list(set(self.vectors))

    def round_vectors(self):
        for i in self.vectors:
            i.round_values()
