import pyglet
from pyglet.gl import *


class graphstyle(pyglet.graphics.Group):
    def __init__(self,state = "DAN",lineweight = 1):
        super().__init__()
        self.state = state
        self.lineweight = lineweight

    def set_state(self):
        glLineWidth(self.lineweight)
        
        if 'D' in self.state:
            # .glEnable(.GL_TEXTURE_2D)
            glShadeModel(GL_SMOOTH)
            glEnable(GL_LINE_SMOOTH)
        
        if 'A' in self.state:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        if 'N' in self.state:
            glHint(GL_LINE_SMOOTH_HINT, GL_NICEST);
    # def unset_state(self):
    #     pass
