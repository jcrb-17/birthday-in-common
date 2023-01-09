import pygame
import Boton

class MenuJuego():
	def __init__(self,screen):
		self.fondo = (10,50,150)
		self.width = 150
		self.height = 50
		self.x = (600,0)
		self.y = (10,0)
		self.botones = [Boton.Boton("EscojerCantidad",self.x[0],self.y[0],self.width,self.height,"Cantidad"),Boton.Boton("MenuInicial",self.x[0]+self.width+10,self.y[0],self.width,self.height,"Menu")]
		self.dibujarBotones(screen)
		self.texto = "Probabilidad cumpleaños en común"
	def dibujarBotones(self,screen):
		for x in self.botones:
			pygame.draw.rect(screen,x.color,x.rect)
	def ponerTexto(self,screen,font):
		for x in self.botones:
			text = font.render(x.text,True,(255,255,200))
			screen.blit(text,[x.rect.x+15, x.rect.y+10])
		text = font.render(self.texto,True,(255,255,220))
		screen.blit(text,(40,20))
