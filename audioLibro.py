from libro import Libro

class AudioLibro(Libro):
	"""docstring for AudioLibro"""
	def __init__(self,titulo = None, editorial = None, anio_publicacion = None, genero = None, edicion = None, precio = None, duracionLibro = None,  listaAtributos = None):
		Libro.__init__(self, titulo, editorial, anio_publicacion, genero, edicion, precio);
		self.duracionLibro = duracionLibro
		pass

	def __str__(self):
		"""Muestra  al AudiLibro"""
		return str(self.titulo) + ", " + str(self.editorial) + ", " + str(self.anio_publicacion) + ", " + str(self.genero) + ", " + str(self.edicion) + ", " + str(self.precio) + ", "+ str(self.duracionLibro);
		

#a = AudioLibro("Dracula", "Porrua", "1998", "Terror", "3Edicion", "315", "1:45")

#print(a)
		