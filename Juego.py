import Estudiante
import Color
import Nombres
import Dias
import Genero
import MenuInicial

class Juego():
	def __init__(self,n):
		self.matches = 0
		self.etudiants = []
		self.genererEtudiants(n)
		self.anniversaireComparaison()
	def commencerJeux(self):
		pass
	def peindreGUI(self):
		pass
	def genererEtudiants(self,quantite):
		for x in range(0,quantite):
			etudiant = Estudiante.Estudiante()
			genre = Genero.Genero()
			etudiant.setGenre(genre.getGenre())
			noms = Nombres.Nombres()
			if etudiant.getGenre() == "Hombre":
				etudiant.setNom(noms.chooseMale())
			if etudiant.getGenre() == "Mujer":
				etudiant.setNom(noms.chooseFemale())
			jour = Dias.Dias()
			etudiant.setAnniversaire(jour.getJourNumero())
			etudiant.setAnniversaireDateFormat(jour.getJourDateFormat())
			self.etudiants.append(etudiant)
	def peindreEtudiants(self):
		pass
	def anniversaireComparaison(self):
		for x in range(0,len(self.etudiants)):
			counterX = 0
			if self.etudiants[x].getAnniversaireInCommon() == True:
				continue
			else:
				color = Color.Color().genererColor()
				for y in range(x+1,len(self.etudiants)):
					if y == len(self.etudiants)-1:
						if counterX>0:
							self.etudiants[x].setAnniversaireInCommon(True)
							self.etudiants[x].setColor(color)
							self.matches +=1
					elif self.etudiants[x].getAnniversaire() == self.etudiants[y].getAnniversaire():
						#self.matches +=1
						self.etudiants[y].setAnniversaireInCommon(True)
						self.etudiants[y].setColor(color)
						counterX+=1

