from persona import Persona


class Femenino(Persona):

    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
        print("Hola Miss " + nombre)