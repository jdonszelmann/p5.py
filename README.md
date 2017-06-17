# p5.py
A p5.js clone written entirely in Python aiming to support the same featureset. 
It is currently a work in progress, see [TODO.md](https://github.com/jonay2000/p5.py/blob/master/TODO.md) for more details about the current progress.

## How to install?
As of writing ther is no pip package available, instead you can clone this repository and take a look at the examples section.
There is no need to include the p5.js package in your `$PATH` environment variable. 
To start out just run: `python test.py` It will search in the current directory for the p5.py package and the package will run the sketch.

## Example
The following example will draw a rotating ball which changes color
```
from p5 import *                # Import all functions from the p5.py package
import math

def setup():                    # The starting point of the sketch
    CreateWindow(640, 480)      # Create the display window
    background(name="white")    # Set the background to white
    caption("hey!")             # Change the title of the window

col = 0
x,y = 0,0
n = True

def draw():                     # The draw function is continuously called to draw each frame
    if n: clear()
    global col, x, y
    fill(math.cos(0.2*col)*255, math.sin(0.2*col)*255, math.tan(0.2*col)*255)   # Set the color of shapes
    translate(math.cos(x)*100+200+math.sin(y-0.2)*25,
        math.atan(y)*100 + 100 + math.sin(x)*50+math.cos(y+3)*50)               # Translate following objects
    rotate(math.cos(y)*TAU)                                                     # Rotate objects
    ellipse(0, 0, abs(math.cos(y)*50)+20, abs(math.sin(x)*30)+20)               # Draw an elllips
    x += 0.05; y += 0.05; col += 0.1                                            # Increase values in loop

def KeyPressed():              # This function is called when a key is pressed
    global n
    if n: n = False
    else: n = True
```

#### Result:
![Animated GIF of the end result](https://github.com/jonay2000/p5.py/blob/master/images/test.gif)