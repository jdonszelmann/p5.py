import pyglet, inspect, importlib.util
from pyglet.gl import *
from p5.Globals import *
from p5.functions import *

class init:
	def __init__(self, setup=None, preload=None, draw=None):
		# list functions from main file to be called
		f = inspect.getouterframes(inspect.currentframe())[-1][1]
		Globals.__FILE__ = f
		print(f)

		#import sketch (from absolute path)
		spec = importlib.util.spec_from_file_location("", Globals.__FILE__)
		sketch = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(sketch)
		
		try:
			self.setup = sketch.setup
		except:
			raise SystemExit("found no setup function! p5.py failed to start.")
		try:
			self.draw = sketch.draw
		except:
			raise SystemExit("could not find draw function, p5.py failed to start.")

		# start p5py
		self.start ()

	def start(self):
		# run setup from sketch
		self.setup ()

		glEnable(GL_TEXTURE_2D)         # enable textures
		glShadeModel(GL_SMOOTH)         # smooth shading of polygons

		while Globals.__RUNNING__:
			dt = pyglet.clock.tick()

			#call draw from sketch
			self.draw()
			#update every window
			for window in windowmanager.windows:
				window.dispatch_events()
				window.clear()
				window.flip()


class _windowmanager:
	def __init__(self):
		self.windows = []
		self.selectedwindow = None

	def new_window(self,w,h,resizable):
		win = pyglet.window.Window(w,h,resizable=True)
		self.windows.append(win)
		if len(self.windows) == 1:
			self.selectedwindow = win
		return win

	def remove(self,window):
		self.windows.remove(window)
		window.close()
		if len(self.windows) == 0:
			Globals.__RUNNING__ = False


class _drawsettings:
	def __init__(self):
		self.settings = {}



class _vectorset:
	def __init__(self, vectors = []):
		self.vectors = vectors

	def __getitem__(self, key):
		return self.vectors[key]
	def __setitem__(self, key, value):
		self.vectors[key] = value

	def scale(self, x=1,y=1,z=1):
		from p5.classes import CreateVector
		scale_vector = CreateVector(x,y,z)
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








windowmanager = _windowmanager()

