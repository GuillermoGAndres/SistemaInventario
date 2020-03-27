from libro import Libro

try:
	baseDatosLibros = open("baseDatosLibros.txt", "r")
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

	print(estructuraDeDatos)
	
except:
	print("Error al abrir")
finally:
	baseDatosLibros.close()