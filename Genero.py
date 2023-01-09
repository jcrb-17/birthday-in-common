import random
class Genero():
	def __init__(self):
		self.genre = random.choice([1,2])
	def getGenre(self):
		if self.genre == 1:
			return "Mujer"
		elif self.genre == 2:
			return "Hombre"
