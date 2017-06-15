import math
from .core import WindowManager

# no dependencies (tkinter is builtin)


# ------------------------------------------------------------------------
# declaration of global vars

class globalvars:
    FPS = 60.0
    FILE = None
    RUNNING = True
    DEFAULTWIDTH = 640
    DEFAULTHEIGHT = 480
    MODE = "2D"
    WINDOWMANAGER = WindowManager()
    KEYPRESSED = False
    ANGLEMODE = "RADIANS"
    RANDOMSEED = 1

# ------------------------------------------------------------------------
# declaration of constants
Globals = globalvars()


# geometry
TAU = math.pi * 2
TWO_PI = math.pi * 2
PI = math.pi
HALF_PI = math.pi / 2
QUARTER_PI = math.pi / 4

class Variable:
	def __init__(self,value):
		self.value = value

	def set(self,value):
		self.value = value

	def get(self,value):
		return self.value

	def __repr__(self):
		return str(self.value)

	def __str__(self):
		return str(self.value)

	def __int__(self):
		try:
			return int(self.value)
		except:
			return 0
	def __lt__(self, other):
		return self.value < other
	
	def __le__(self, other):
		return self.value <= other
	
	def __eq__(self, other):
		return self.value == other
	
	def __ne__(self, other):
		return self.value != other
	
	def __gt__(self, other):
		return self.value > other
	
	def __ge__(self, other):
		return self.value >= other

keycode = Variable(None)
key = Variable(None)
modifiers = Variable(None)
keyispressed = Variable(False)
