from persona import Persona

class Masculino(Persona): # Heredamos de Persona

	def __init__(self, nombre, genero):
		self.nombre = nombre
		self.genero = genero
		print("Hola mister "+nombre)