from femenino import Femenino
from masculino import Masculino

class Factoria(object):


	def get_persona(self, nombre, genero):
		"""Metodo que retorna objetos persona segun el genero"""

		#genero es el parametro usado por la factoria
		#para elegir el obj a crear
		if (genero is 'F'):
			return Femenino(nombre, genero)
		elif (genero is 'M'):
			return Masculino(nombre, genero)