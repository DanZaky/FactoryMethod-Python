##Clase que define a una persona

class Persona(object):

	def __init__(self):
		self.nombre = None
		self.genero = None


	def get_nombre(self):
		return self.nombre

	def get_genero(self):
		return self.genero

	def __str__(self):
		return "Informacion de una persona:\n1. Nombre: {n}\n2. Genero: {g}".format(n=self.get_nombre(), g=self.get_genero())