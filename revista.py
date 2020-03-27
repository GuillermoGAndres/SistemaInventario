
class Revista():

	def __init__(self, titulo = None, tipoRevista = None, entidad = None, fecha = None, precio = None,  listaAtributos = None):
		
		if listaAtributos != None:
			self.titulo = listaAtributos[0]
			self.tipoRevista = listaAtributos[1]
			self.entidad = listaAtributos[2]
			self.fecha = listaAtributos[3]
			self.precio = listaAtributos[4]
		else:
			self.titulo = titulo	
			self.tipoRevista = tipoRevista
			self.entidad = entidad
			self.fecha = fecha
			self.precio = precio
		pass

	def __str__(self):
		return str(self.titulo) + ", " + str(self.tipoRevista) + ", " + str(self.entidad) + ", " + str(self.fecha) + ", " + str(self.precio);

#print(Revista("Nasa en el espacio", "Ciencias", "UNAM", "25/06/1998", "58"))