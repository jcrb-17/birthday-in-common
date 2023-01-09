import pygame
import Boton
class MenuEscojerCantidad():
	def __init__(self,screen):
		self.fondo = (10,50,150)
		self.width = 100
		self.height = 100
		self.x = (280,430,580)
		self.y = (100,300,500)
		self.botones = [Boton.Boton("10",self.x[0],self.y[0],self.width,self.height,"10"),Boton.Boton("20",self.x[1],self.y[0],self.width,self.height,"20"),Boton.Boton("30",self.x[2],self.y[0],self.width,self.height,"30"),Boton.Boton("40",self.x[0],self.y[1],self.width,self.height,"40"),Boton.Boton("50",self.x[1],self.y[1],self.width,self.height,"50"),Boton.Boton("60",self.x[2],self.y[1],self.width,self.height,"60"),Boton.Boton("70",self.x[0],self.y[2],self.width,self.height,"70"),Boton.Boton("80",self.x[1],self.y[2],self.width,self.height,"80"),Boton.Boton("90",self.x[2],self.y[2],self.width,self.height,"90")]
		self.dibujarBotones(screen)
		self.texto = "Elija la cantidad de personas"
	def dibujarBotones(self,screen):
		for x in self.botones:
			pygame.draw.rect(screen,x.color,x.rect)
	def ponerTexto(self,screen,font):
		for x in self.botones:
			text = font.render(x.text,True,(255,255,200))
			screen.blit(text,[x.rect.x+35, x.rect.y+35])
		text = font.render(self.texto,True,(255,255,220))
		screen.blit(text,(260,20))
