
class Juguete():

	def __init__(self, nombre = None, material = None, precio = None, listaAtributos = None):

		if(listaAtributos != None):
			self.nombre = listaAtributos[0]
			self.material = listaAtributos[1]
			self.precio = listaAtributos[2]
		else:
			self.nombre = nombre
			self.material = material
			self.precio = precio
		pass
	def __str__(self):
		"""Muestra  al Libro"""
		return str(self.nombre) + ", " + str(self.material) + ", " + str(self.precio);
	pass
	pass

#print(Juguete("Goku", "Plastico", "250"))