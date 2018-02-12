"""
Clase que define a una persona
"""

class Persona(object):
	"""Para nuestro caso, una persona tendra un nombre,
	una edad y un genero. """
	def __init__(self, nombre, edad, genero): #<- Constructor
		self.nombre = nombre
		self.edad = edad
		self.genero = genero

	# Algunos getters ...
	def get_nombre(self):
		return self.nombre

	def get_edad(self):
		return self.edad

	def get_genero(self):
		return self.genero

	# Algunos setters ...
	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_edad(self, edad):
		self.edad = edad
	
	def set_genero(self, genero):
		self.genero = genero
	
	def saludar(self, saludo):
		return saludo

	def __str__(self):
		return "Informacion de una persona:\n1. Nombre: {n}\n2. Edad: {e}\n3. Genero: {g}".format(
			n=self.get_nombre(), e=self.get_edad(), g=self.get_genero())