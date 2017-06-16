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
    storesettings = []
    def __init__(self):
        from p5.classes import Color,Vector,Font
        # color related properties
        self.stroke = Color(0,0,0)
        self.backgroundcolor = Color(51)
        self.fillcolor = Color(255, 255, 255)
        # value related properties
        self.strokeweight = 1
        self.rectmode = "CORNER"
        self.translate = Vector(0,0)
        self.rotate = 0
        self.ellipsemode = "CENTER"
        self.font = Font()

    def push(self):
        self.storesettings.insert(0,{key:value for key, value in self.__dict__.items() if not key.startswith('__') and not callable(key)})

    def pop(self):
        a = self.storesettings.pop()
        for key,value in a.items():
            setattr(self,key,value)

    def reset(self):
        from p5.classes import Color,Vector,Font

        self.stroke = Color(0,0,0)
        self.backgroundcolor = Color(51)
        self.fillcolor = Color(255, 255, 255)
        # value related properties
        self.strokeweight = 1
        self.rectmode = "CORNER"
        self.translate = Vector(0,0)
        self.rotate = 0
        self.ellipsemode = "CENTER"
        self.font = Font()


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
    def __init__(self,state = "DAN",lineweight = 1):
        super().__init__()
        self.state = state
        self.lineweight = lineweight

    def set_state(self):
        pyglet.gl.glLineWidth(self.lineweight)
        
        if 'D' in self.state:
            # pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
            pyglet.gl.glShadeModel(pyglet.gl.GL_SMOOTH)
            pyglet.gl.glEnable(pyglet.gl.GL_LINE_SMOOTH)
        
        if 'A' in self.state:
            pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
            pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        if 'N' in self.state:
            pyglet.gl.glHint(pyglet.gl.GL_LINE_SMOOTH_HINT, pyglet.gl.GL_NICEST);
    # def unset_state(self):
    #     pass



