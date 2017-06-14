import pyglet
from pyglet.gl import *

class WindowManager:
    def __init__(self):
        self.windows = []
        self.selectedwindow = None

    def add(self, window):
        self.windows.append(window)
        if len(self.windows) == 1:
            self.selectedwindow = window

    def remove(self, window):
        from .globals import Globals
        self.windows.remove(window)
        if len(self.windows) == 0:
            Globals.RUNNING = False


class DrawSettings:
    def __init__(self):
        from p5.classes import Color
        # color related properties
        self.strokecolor = Color(255, 255, 255)
        self.backgroundcolor = Color(255, 0, 255)
        self.fillcolor = Color(255, 255, 255)
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
	s = _vectorset(Vector(0,0),Vector(5,5))
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

"""
D = Default = enable textures and smoothen lines
A = Alpha = enable alpha (opacity)


"""

class graphstyle(pyglet.graphics.Group):
    def __init__(self,state = "DA",lineweight = 1):
        super().__init__()
        self.state = state
        self.lineweight = lineweight

    def set_state(self):
        pyglet.gl.glLineWidth(self.lineweight)
        
        if 'D' in self.state:
            pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
            pyglet.gl.glShadeModel(pyglet.gl.GL_SMOOTH)
        
        if 'A' in self.state:
            pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
            pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

    # def unset_state(self):
    #     pass



