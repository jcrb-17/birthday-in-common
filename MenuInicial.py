import pygame
import Boton
class MenuInicial():
	def __init__(self,screen):
		self.fondo = (10,50,150)
		x = 410
		y = 210
		w = 145
		h= 50
		self.botones = [Boton.Boton("Iniciar",x,y,w,h," Iniciar "),Boton.Boton("AcercaDe",x,y+100,w,h,"Acerca De"),Boton.Boton("Salir",x,y+200,w,h,"  Salir ")]
		self.dibujarBotones(screen)
	def dibujarBotones(self,screen):
		for x in self.botones:
			pygame.draw.rect(screen,x.color,x.rect)
	def ponerTexto(self,screen,font):
		for x in self.botones:
			text = font.render(x.text,True,(255,255,200))
			screen.blit(text,[x.rect.x+5, x.rect.y+12])
