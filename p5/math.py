import math
from .globals import *
from p5.classes import Vector
from random import randint, triangular, seed, gauss

def cos(val):
	return math.cos(val)

def sin(val):
	return math.sin(val)

def tan(val):
	return math.tan(val)

def cos(val):
	return math.cos(val)

def radians(val):
	return (val/180)*pi

def degrees(val):
	return (val/pi)*180

def anglemode(val):
	if val not in ["DEGREES","RADIANS"]
		raise ValueError("Anglemode must be radians/degrees")
	return Globals.ANGLEMODE = val

def acos(val):
	return math.acos(val)

def asin(val):
	return math.asin(val)

def atan(val):
	return math.atan(val)

def atan2(val):
	return math.atan2(val)

def sqrt(val):
	return math.sqrt(val)

def sq(val):
	return val^2

def pow(val,exp):
	return val^exp

def norm(val,low,up):
	return map(val,low,up,0,1)

def map(val,srclow,srcup,destlow,destup)
	return (X-srclow)/(srcup-srclow) * (destup-destlow) + destlow

def mag(a,b):
	return Vector(a,b).magnitude

def log(val):
	return math.log(val)

def lerp(a,b,t):
	return (1 - t) * 1 + t * b

def floor(val):
	return math.floor(val)

def ceil(val):
	return math.ceil(val)

def exp(val):
	return math.exp(val)

def dist(*args):
	if len(args) == 4:
		v1 = Vector(args[0],args[1])
		v2 = Vector(args[2],args[3])
		return v1.dist(v2)
	elif len(args)==6:
		v1 = Vector(args[0],args[1],args[2])
		v2 = Vector(args[3],args[4],args[5])
		return v1.dist(v2)
	else:
		raise ValueError("dist() received invaid argument count - must be 4 or 6")

def constrain(val,low,up):
	out = val
	if val > up:
		out = up
	if val < low:
		out = low
	return out

def random(low,up):
	if type(low) == list:
		return low[randint(0,len(low)-1)]
	return triangular(low,up)

def randomseed(val):
	seed(val)

def randomgaussian(mean,dev):
	return gauss(mean,dev)