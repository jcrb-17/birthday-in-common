import pygame
import Juego
import MenuInicial
import MenuEscojerCantidad
import MenuJuego

pygame.init()

#Assets
imagesFemale = [pygame.image.load("imagenes/mujer/1.png"),pygame.image.load("imagenes/mujer/2.png"),pygame.image.load("imagenes/mujer/3.png"),pygame.image.load("imagenes/mujer/4.png"),pygame.image.load("imagenes/mujer/5.png"),pygame.image.load("imagenes/mujer/6.png"),pygame.image.load("imagenes/mujer/7.png"),pygame.image.load("imagenes/mujer/8.png"),pygame.image.load("imagenes/mujer/9.png"),pygame.image.load("imagenes/mujer/10.png"),pygame.image.load("imagenes/mujer/11.png"),pygame.image.load("imagenes/mujer/12.png")]
imagesMale = [pygame.image.load("imagenes/hombre/1.png"),pygame.image.load("imagenes/hombre/2.png"),pygame.image.load("imagenes/hombre/3.png"),pygame.image.load("imagenes/hombre/4.png"),pygame.image.load("imagenes/hombre/5.png"),pygame.image.load("imagenes/hombre/6.png"),pygame.image.load("imagenes/hombre/7.png"),pygame.image.load("imagenes/hombre/8.png"),pygame.image.load("imagenes/hombre/9.png"),pygame.image.load("imagenes/hombre/10.png"),pygame.image.load("imagenes/hombre/11.png"),pygame.image.load("imagenes/hombre/12.png")]
imageAbout = pygame.image.load("imagenes/acercaDe.png")
icon = pygame.image.load("imagenes/icon.png")
width = 1000
height = 700
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Cumpleaños en Común")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Monospace",25,True,False)

encendido = True
estado = "MenuInicial"

def getProbability(n):
	n1 = 364
	n2 = 364
	val = 1
	for x in range(0,n):
		val *= n1/n2
		n1 -=1
	return 1-val
def getCollisionBetween2Rect(rect1,rect2):
	return rect1.colliderect(rect2)
def getCollisionMenuButton(menu,rect):
	for x in menu.botones:
		if rect.colliderect(x):
			return x.tipo
	return None
def drawPeople(screen,listaDePersonas):
	posX = [50,110,170,230,290,350,410,470,530,590]
	posY = [90,150,210,270,330,390,450,510,570,630]
	counterX = 0
	counterY = 0
	for x in listaDePersonas:
		if counterX == 10:
			counterX = 0
			counterY += 1
		x.rect.x = posX[counterX]
		x.rect.y = posY[counterY]
		if x.color == None:
			pygame.draw.rect(screen,(10,10,10),x.rect)
		else:
			pygame.draw.rect(screen,x.color,x.rect)
		if x.getGenre() == "Mujer":
			screen.blit(imagesFemale[x.getImageNumber()-1],(x.rect.x,x.rect.y))
		if x.getGenre() == "Hombre":
			screen.blit(imagesMale[x.getImageNumber()-1],(x.rect.x,x.rect.y))
		counterX+=1
def drawPeopleInfo(screen,name,anniversaireDF):
	nameXPos = 700
	nameYPos = 160
	anniversaireDFXPos = 700
	anniversaireDFYPos = 220
	text1 = font.render(name,True,(255,255,200))
	screen.blit(text1,[nameXPos,nameYPos])
	text2 = font.render(anniversaireDF,True,(255,255,200))
	screen.blit(text2,[anniversaireDFXPos,anniversaireDFYPos])
def drawMatches(screen,matches):
	text1 = font.render("Cantidad",True,(255,255,200))
	screen.blit(text1,[700,300])
	text2 = font.render(str(matches),True,(255,255,200))
	screen.blit(text2,[700,340])
def drawProbability(screen,estudiantes):
	text1 = font.render("Probabilidad",True,(255,255,200))
	screen.blit(text1,[700,410])
	text2 = font.render(str(getProbability(len(estudiantes)))[0]+str(getProbability(len(estudiantes)))[1]+str(getProbability(len(estudiantes)))[2]+str(getProbability(len(estudiantes)))[3],True,(255,255,200))
	screen.blit(text2,[700,460])
menu = None
menu2 = MenuEscojerCantidad.MenuEscojerCantidad(screen)
menu3 = MenuJuego.MenuJuego(screen)

buttonX = pygame.Rect(855,70,50,50)
#Juego Class
estudiantes = []
matches = 0
juego = None

while encendido:
	screen.fill((10,10,10))
	mousePos = pygame.mouse.get_pos()
	mousePosRect = pygame.Rect(mousePos[0]-5,mousePos[1]-5,1,1)
	if estado == "MenuInicial":
		estudiantes = []
		matches = 0
		menu = MenuInicial.MenuInicial(screen)
		menu.ponerTexto(screen,font)
		text = font.render("Cumpleaños en común",True,(255,255,200))
		screen.blit(text,(340,80))
		text = font.render("Probabilidad",True,(255,255,200))
		screen.blit(text,(390,120))
	elif estado == "Iniciar":
		menu = None
		estudiantes = []
		matches = 0
		menu2.dibujarBotones(screen)
		menu2.ponerTexto(screen,font)
	elif estado == "Juego":
		menu = None
		menu3.dibujarBotones(screen)
		menu3.ponerTexto(screen,font)
		if len(estudiantes) == 0:
			juego = Juego.Juego(int(numberSelected))
			matches = juego.matches
			estudiantes = juego.etudiants
		w = 0
		drawPeople(screen,estudiantes)
		for x in estudiantes:
			if mousePosRect.colliderect(x.rect):
				drawPeopleInfo(screen,x.getNom(),x.getAnniversaireDateFormat())
		drawMatches(screen,matches)
		drawProbability(screen,estudiantes)
	elif estado == "AcercaDe":
		menu = None
		screen.blit(imageAbout,(0,0))
		pygame.draw.rect(screen,(255,0,100),buttonX)
		text = font.render("X",True,(255,255,200))
		screen.blit(text,[855+16, 70+12])
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			encendido = False
		if estado == "MenuInicial":
			if e.type == pygame.MOUSEBUTTONDOWN and getCollisionMenuButton(menu,mousePosRect):
				if getCollisionMenuButton(menu,mousePosRect) == "Salir":
					encendido = False
				if getCollisionMenuButton(menu,mousePosRect) == "Iniciar":
					estado = "Iniciar"
				if getCollisionMenuButton(menu,mousePosRect) == "AcercaDe":
					estado = "AcercaDe"
		if e.type == pygame.MOUSEBUTTONDOWN and estado == "Iniciar" and getCollisionMenuButton(menu2,mousePosRect):
			numberSelected = getCollisionMenuButton(menu2,mousePosRect)
			estado = "Juego"
		if e.type == pygame.MOUSEBUTTONDOWN and estado == "Juego" and getCollisionMenuButton(menu3,mousePosRect):
			if getCollisionMenuButton(menu3,mousePosRect) == "EscojerCantidad":
				estado = "Iniciar"
			if getCollisionMenuButton(menu3,mousePosRect) == "MenuInicial":
				estado = "MenuInicial"
		if e.type == pygame.MOUSEBUTTONDOWN and estado == "AcercaDe" and buttonX.colliderect(mousePosRect):
			estado = "MenuInicial"
	pygame.draw.rect(screen,(10,10,10),mousePosRect)
	pygame.display.flip()
	clock.tick(30)
pygame.quit()
