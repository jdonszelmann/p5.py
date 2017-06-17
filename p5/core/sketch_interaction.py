
class sketch:
    def __init__(self):
        from ..globals import Globals
        self.sketch = Globals.FILE
        self.present = {"SETUP":True,"DRAW":True,"MOUSEDRAG":True,"MOUSEPRESS":True,"KEYDOWN":True,"KEYUP":True,"KEYTYPE":True}


    def draw(self):
        try:
            self.sketch.draw()
        except AttributeError:
            if self.present["DRAW"]:
                print("[p5.py Error]: no setup() fucnction present (required but not vital)")
                self.present["DRAW"] = False

    def setup(self):
        try:
            self.sketch.setup()
        except AttributeError:
            if self.present["SETUP"]:
                print("[p5.py Error]: no setup() fucnction present (required but not vital)")
                self.pre

    def mousedragged(self):
        try:
            self.sketch.MouseDragged()
        except AttributeError:
            if self.present["MOUSEDRAG"]:
                print("[p5.py Notification]: no MouseDragged() fucnction present (not required)")  
                self.present["MOUSEDRAG"] = False

    def keypressed(self):
        try:
            self.sketch.KeyPressed()
        except AttributeError:
            if self.present["KEYDOWN"]:
                print("[p5.py Notification]: no KeyPressed() fucnction present (not required)")  
                self.present["KEYDOWN"] = False

    def keyreleased(self):
        try:
            self.sketch.KeyReleased()
        except AttributeError:
            if self.present["KEYUP"]:
                print("[p5.py Notification]: no KeyReleased() fucnction present (not required)") 
                self.present["KEYUP"] = False 

    def mousepressed(self):
        try:
            self.sketch.MousePressed()
        except AttributeError:
            if self.present["MOUSEPRESS"]:
                print("[p5.py Notification]: no MousePressed() fucnction present (not required)")  
                self.present["MOUSEPRESS"] = False

    def keytyped(self):
        try:
            self.sketch.KeyTyped()
        except AttributeError:
            if self.present["KEYTYPE"]:
                print("[p5.py Notification]: no KeyTyped() fucnction present (not required)")  
                self.present["KEYTYPE"] = False