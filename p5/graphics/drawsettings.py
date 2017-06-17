


class DrawSettings:
    storesettings = []
    def __init__(self):
        from .color import Color
        from ..math.vector import Vector
        from .font import Font
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
        from .color import Color
        from ..math import Vector
        from .font import Font

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