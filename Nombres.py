import random
class Nombres():
	def __init__(self):
		self.femenin = ["María","Guadalupe","Juana","Margarita","Josefina","Verónica","Elena","Leticia","Rosa","Francisca","Teresa","Alicia","Fernanda","Alejandra","Martha","Yolanda","Patricia","Elisa","Gloria","Gabriela","Silvia","Ana","Luisa","Antonia","Araceli","Andrea","Isabel","Irma","Carmen","Lucía","Adriana","Lupe","Luna","Miranda","Angelina","Bianca","Malena","Carolina","Aida","Olivia","Lola","Paloma","Vanessa","Adela","Alexa","Aracely","Bárbara","Candela","Jacinta","Sara"]
		self.masculin = ["Juan","Luis","José","Francisco","Antonio","Jesús","Miguel","Ángel","Pedro","Alejandro","Manuel","Carlos","Roberto","Fernando","Daniel","Jorge","Ricardo","Eduardo","Javier","Rafael","Martín","Raúl","David","Arturo","Marco","Enrique","Gerardo","Mario","Alfredo","Sergio","Armando","Santiago","Salvador","Víctor","Gabriel","Andrés","Óscar","Guillermo","Ramón","Pablo","Rubén","Felipe","Jaime","Julio","César","Diego","Gustavo","Agustín","Esteban","Santos"]
	def chooseMale(self):
		return random.choice(self.masculin)
	def chooseFemale(self):
		return random.choice(self.femenin)
