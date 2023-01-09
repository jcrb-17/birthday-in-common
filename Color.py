import random
class Color():
	def __init__(self):
		pass
	def genererColor(self):
		r = random.randrange(30,256)
		g = random.randrange(30,256)
		b = random.randrange(30,256)
		color = [r,g,b]
		return color
