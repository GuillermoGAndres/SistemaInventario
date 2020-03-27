#Esta sera la base datos central como el script que obtendras los datos de cada
#base de datos de libros, revistas, audioLibros, Juquetes, y regresara
#cada objeto dentro de un estructura de datos
from libro import Libro
from revista import Revista
from audioLibro import AudioLibro
from juguete import Juguete

def obtenerBaseDatosLibros(ruta):
	try:
		baseDatosLibros = open(ruta, "r")
		estructuraDeDatos = []
		linea = baseDatosLibros.readline()
		#print(linea)
		#print(type(linea))
		#1raForma de hacerlo metodo slip() para cadenas 
		#listaPalbras2daForma = linea.split(sep = ',')
		#print(listaPalbras2daForma)
		#2daForma de hacer
		#Si no existiera el split()->String seria hacerlo manual:
		while(linea):
			palabra = ''
			listaPalabras = []
			count = 0
			for char in linea:
				count += 1 #Esto es porque al final no termina en ',' por lo tanto no se guarda la ultima palabra,
						   #existen varias formas de corregirlo una es modificar el toString de libro y que termine en ',' o esta forma saber cual es la ultima linea
				if char == ',':
					listaPalabras.append(palabra)
					palabra = '' #inicializo nuevamente en ceros
				elif char == ' ':
					#Como tambien puse despues de la coma un espacio
					#tambien hay que eliminarlo
					pass
				elif count == len(linea): #con esto identificamos cual es la ultima linea,
					#y agregamos la ultima palabra que falta, significa que ya no hay mas char que leer termino de leer, 
					#print("entro")
					listaPalabras.append(palabra)
					pass
				else:
					palabra += char


			#print(listaPalabras)
			book = Libro(listaAtributos = listaPalabras);
			#print(book)
			estructuraDeDatos.append(book)
			linea = baseDatosLibros.readline()

		#print(estructuraDeDatos)
		return estructuraDeDatos
		
	except:
		print("Error al abrir")
		#return None
	finally:
		baseDatosLibros.close()
		#return None

def obtenerBaseDatosRevista(ruta):
	try:
		archivo = open(ruta, "r")
		estructuraDeDatos = []
		linea = archivo.readline()
		#print(linea)
		#print(type(linea))
		#1raForma de hacerlo metodo slip() para cadenas 
		#listaPalbras2daForma = linea.split(sep = ',')
		#print(listaPalbras2daForma)
		#2daForma de hacer
		#Si no existiera el split()->String seria hacerlo manual:
		while(linea):
			palabra = ''
			listaPalabras = []
			count = 0
			for char in linea:
				count += 1 #Esto es porque al final no termina en ',' por lo tanto no se guarda la ultima palabra,
						   #existen varias formas de corregirlo una es modificar el toString de libro y que termine en ',' o esta forma saber cual es la ultima linea
				if char == ',':
					listaPalabras.append(palabra)
					palabra = '' #inicializo nuevamente en ceros
				elif char == ' ':
					#Como tambien puse despues de la coma un espacio
					#tambien hay que eliminarlo
					pass
				elif count == len(linea): #con esto identificamos cual es la ultima linea,
					#y agregamos la ultima palabra que falta, significa que ya no hay mas char que leer termino de leer, 
					#print("entro")
					listaPalabras.append(palabra)
					pass
				else:
					palabra += char


			#print(listaPalabras)
			magazine = Revista(listaAtributos = listaPalabras);
			#print(book)
			estructuraDeDatos.append(magazine)
			linea = archivo.readline()

		#print(estructuraDeDatos)
		return estructuraDeDatos
		
	except:
		print("Error al abrir")
		#return None
	finally:
		archivo.close()
		#return None

def obtenerBaseDatosAudioLibro(ruta):
	try:
		archivo = open(ruta, "r")
		estructuraDeDatos = []
		linea = archivo.readline()
		#print(linea)
		#print(type(linea))
		#1raForma de hacerlo metodo slip() para cadenas 
		#listaPalbras2daForma = linea.split(sep = ',')
		#print(listaPalbras2daForma)
		#2daForma de hacer
		#Si no existiera el split()->String seria hacerlo manual:
		while(linea):
			palabra = ''
			listaPalabras = []
			count = 0
			for char in linea:
				count += 1 #Esto es porque al final no termina en ',' por lo tanto no se guarda la ultima palabra,
						   #existen varias formas de corregirlo una es modificar el toString de libro y que termine en ',' o esta forma saber cual es la ultima linea
				if char == ',':
					listaPalabras.append(palabra)
					palabra = '' #inicializo nuevamente en ceros
				elif char == ' ':
					#Como tambien puse despues de la coma un espacio
					#tambien hay que eliminarlo
					pass
				elif count == len(linea): #con esto identificamos cual es la ultima linea,
					#y agregamos la ultima palabra que falta, significa que ya no hay mas char que leer termino de leer, 
					#print("entro")
					listaPalabras.append(palabra)
					pass
				else:
					palabra += char


			#print(listaPalabras)
			audiobook = AudioLibro(listaPalabras[0], listaPalabras[1], listaPalabras[2], listaPalabras[3], listaPalabras[4], listaPalabras[5], listaPalabras[6]);
			#print(book)
			estructuraDeDatos.append(audiobook)
			linea = archivo.readline()

		#print(estructuraDeDatos)
		return estructuraDeDatos
		
	except:
		print("Error al abrir")
		#return None
	finally:
		archivo.close()

def obtenerBaseDatosJuguete(ruta):
	try:
		archivo = open(ruta, "r")
		estructuraDeDatos = []
		linea = archivo.readline()
		#print(linea)
		#print(type(linea))
		#1raForma de hacerlo metodo slip() para cadenas 
		#listaPalbras2daForma = linea.split(sep = ',')
		#print(listaPalbras2daForma)
		#2daForma de hacer
		#Si no existiera el split()->String seria hacerlo manual:
		while(linea):
			palabra = ''
			listaPalabras = []
			count = 0
			for char in linea:
				count += 1 #Esto es porque al final no termina en ',' por lo tanto no se guarda la ultima palabra,
						   #existen varias formas de corregirlo una es modificar el toString de libro y que termine en ',' o esta forma saber cual es la ultima linea
				if char == ',':
					listaPalabras.append(palabra)
					palabra = '' #inicializo nuevamente en ceros
				elif char == ' ':
					#Como tambien puse despues de la coma un espacio
					#tambien hay que eliminarlo
					pass
				elif count == len(linea): #con esto identificamos cual es la ultima linea,
					#y agregamos la ultima palabra que falta, significa que ya no hay mas char que leer termino de leer, 
					#print("entro")
					listaPalabras.append(palabra)
					pass
				else:
					palabra += char


			#print(listaPalabras)
			toy = Juguete(listaAtributos = listaPalabras);
			#print(book)
			estructuraDeDatos.append(toy)
			linea = archivo.readline()

		#print(estructuraDeDatos)
		return estructuraDeDatos
		
	except:
		print("Error al abrir")
		#return None
	finally:
		archivo.close()
		#return None
#obtenerBaseDatosLibros("baseDatosLibros.txt")
#obtenerBaseDatosRevista("baseDatosRevista.txt")
#obtenerBaseDatosAudioLibro("baseDatosAudioLibros.txt")
#obtenerBaseDatosJuguete("baseDatosJuguetes.txt")