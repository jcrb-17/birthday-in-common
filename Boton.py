import pygame
class Boton():
	def __init__(self,tipo,xpos,ypos,width,height,texto):
		self.tipo = tipo
		self.rect = pygame.Rect(xpos,ypos,width,height)
		self.text = texto
		self.color = (10,50,120)
