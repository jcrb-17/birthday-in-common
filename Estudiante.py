import pygame
import random
class Estudiante():
	def __init__(self):
		self.nom = None
		self.anniversaire = None
		self.anniversaireDateFormat = None
		self.genre = None
		self.anniversaireInCommon = False
		self.color = None
		self.rect = pygame.Rect(0,0,50,50)
		self.imageNumber = random.randrange(1,13)
	#""""""""Setters""""""""""""""""
	def setNom(self,nom):
		self.nom = nom
	def setAnniversaire(self,nom):
		self.anniversaire = nom
	def setAnniversaireDateFormat(self,nom):
		self.anniversaireDateFormat = nom
	def setGenre(self,nom):
		self.genre = nom
	def setAnniversaireInCommon(self,nom):
		self.anniversaireInCommon = nom
	def setColor(self,nom):
		self.color = nom
	#""""""""Getters""""""""""""""""
	def getNom(self):
		return self.nom
	def getAnniversaire(self):
		return self.anniversaire 
	def getAnniversaireDateFormat(self):
		return self.anniversaireDateFormat
	def getGenre(self):
		return self.genre
	def getAnniversaireInCommon(self):
		return self.anniversaireInCommon
	def getColor(self):
		return self.color
	def getImageNumber(self):
		return self.imageNumber
