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

# ------------------------------------------------------------------------
# declaration of constants
Globals = globalvars()


# geometry
TAU = math.pi * 2
TWO_PI = math.pi * 2
PI = math.pi
HALF_PI = math.pi / 2
QUARTER_PI = math.pi / 4
