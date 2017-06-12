import pyglet

def CreateVector(*args,**kwargs):
	from p5.classes import Vector
	return Vector(*args,**kwargs)


# def rect(x1,y1,x2,y2):
# 	
def point(x,y):
	 pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
			('v2i', (x,y)),
			('c3B', (255,255,255))
	)






#drawing propertird such as basckround, fill, stroke etc.
def background(*args,**kwargs):
	from p5.classes import color
	from p5.core import windowmanager

	for i in args:
		if type(i) == color:
			windowmanager.selectedwindow.drawsettings.backgroundcolor = color
			return
	for key,value in kwargs.items():
		if type(value) == color:
			windowmanager.selectedwindow.drawsettings.backgroundcolor = value
			return
	windowmanager.selectedwindow.drawsettings.backgroundcolor = color(*args,**kwargs)
	

def clear():
	from p5.core import windowmanager
	windowmanager.selectedwindow.window.clear()