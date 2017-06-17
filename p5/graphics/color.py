class Color:
    def __init__(self, r: int = None, g: int = None, b: int = None, a: int = 255, name: str = None):
        self.r = r
        self.g = g
        self.b = b
        if self.r == None and self.g == None and self.b == None and name == None:
            self.r = 51
        if self.r != None and self.g == None and self.b == None and name == None:
            self.g = self.r
        if self.r != None and self.g != None and self.b == None and name == None:   
            self.b = self.g
        self.a = a
        if name != None:
            from p5.color import Colors
            self.r, self.g, self.b = Colors.getname(name)



    def get(self, retfloat=False):
        if retfloat:
            return (self.r / 255, self.g / 255, self.b / 255, self.a / 255)
        else:
            return (self.r, self.g, self.b, self.a)


       