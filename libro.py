
class Libro():

	def __init__(self, titulo = None, editorial = None, anio_publicacion = None, genero = None, edicion = None, precio = None, listaAtributos = None):
		'''Estoy aplicando sobrecarga de constructores(overloading) por eso precisamente cada atrubuto le pongo un 
			valor por defecto en esta caso None, porque en python no puede existir 2 metodos que se llaven igulae o constructores
			al poner valores po defecto hago que el metodo sea mas generico, es decir, que pueda aceptar a la vez una lista de atributos
			o atributos suelto'''

		if listaAtributos != None:
			#print("Entro1")
			#for atributo in listaAtributos:
			#	print(atributo)
			#Como sabemos que que lista de atributos solo puede tener 5 atributos, si no solo tendriamos 
			#que reajustar con un if que solo se pueden aceptar 5 atributos
			#Precondion-> la lista de atributos contine 5
			self.titulo = listaAtributos[0]
			self.editorial = listaAtributos[1]
			self.anio_publicacion = listaAtributos[2]
			self.genero = listaAtributos[3]
			self.edicion = listaAtributos[4]
			self.precio = listaAtributos[5]
		else:
			#print("Entro2")
			self.titulo = titulo
			self.editorial = editorial
			self.anio_publicacion = anio_publicacion
			self.genero = genero
			self.edicion = edicion
			self.precio = precio
		pass

	def __str__(self):
		"""Muestra  al Libro"""
		return str(self.titulo) + ", " + str(self.editorial) + ", " + str(self.anio_publicacion) + ", " + str(self.genero) + ", " + str(self.edicion) + ", " + str(self.precio);
	pass