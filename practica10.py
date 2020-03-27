#Para revisar el formato de codificación del sistema se puede utilizar las siguientes líneas
#import locale
#print(locale.getpreferredencoding())


#Abrir un archivo

try:
	
	archivo = open("C:/Users/gerar/Documents/eda2_2019/practica10/prueba.txt", mode = "r", encoding = "utf-8")
	#for linea in archivo:
	#	print(linea)
	linea = archivo.readline()
	while(linea):
		print(linea)
		linea = archivo.readline()

	
	#Ejercicio 1
	#Realizar operacion
	#text = archivo.read();
	#print(text)
	#text = archivo.read();
	#print(text)
	
	#Ejercicio2
	#while True:
	#	linea = archivo.readline()
	#	if not linea:
	#		break
	#	print(linea)

	#Ejercicio3
	#El método readlines() lee todas las líneas de un archivo como una lista. Si se indica el parámetro de tamaño leerá esa cantidad de bytes del archivo y lo necesario hasta completar la última línea
	'''lineas = archivo.readlines()
	numlinea = 0
	print(lineas)
	for linea in lineas:
		numlinea += 1
		print(numlinea, linea)
	archivo.close()'''

	#Ejercio 4
	#La sentencia with-as permite usar los archivos de forma óptima cerrándolos y liberando la memoria al concluir el proceso de lectura
	#with open("prueba.txt","r") as archivo:
	#	for linea in archivo:
	#		print(linea)

	#Ejercicio 5
	"""
	cadena1 = "informacion"
	cadena2 = "random"
	archivo = open("datos2.txt","w")
	cadena1 += "\n"
	archivo.write(cadena1)
	lista = ["manzanas", "pera","frijoles"]
	archivo.writelines(lista)
	archivo.close()"""

	#Ejercicio 6
	#archivo.seek(7)
	#cad = archivo.read(5)
	#print(archivo.tell())

	#Ejercicio 7
	'''import pickle
	lista = ["algoritmos1", "algoritmos2", "datos"]
	archivo = open("materias.txt","wb")
	pickle.dump(lista,archivo)
	archivo.close()
	del lista
	archivo = open("materias.txt","rb")
	lista = pickle.load(archivo)
	print(lista)
	archivo.close()'''

	#Ejercicio 8 crear directorio
	#import os
	#def creardirectorio(ruta):
	#	try:
	#		os.makedirs(ruta)
	#	except OSError:
	#		pass
	#	os.chdir(ruta)
#
#	creardirectorio("C:/Users/gerar/Documents/eda2_2019/practica10/nuevo")
	
	#Ejercicio 9  recorrer un directorio
	#import os
	#"C:/Users/gerar/Documents/eda2_2019/practica10
	#rootDir = "C:/Users/gerar/Documents/eda2_2019/practica10"
	#for dirName, subdirList, fileList in os.walk(rootDir):
	#	print("directorio encontrado: %s" % dirName)
	#	for  fname in fileList:
	#	 	print("\t%s" % fname)

	#Ejercicio 10
	'''archivo = open("prueba.txt", "r")
	contenido = archivo.read()
	nombre = archivo.name
	modo = archivo.mode
	encoding = archivo.encoding
	archivo.close() #Cierra el archivo
	#archivo.close solo es un atributo

	if archivo.closed:
		print("SE ha cerrado")
	else:
		print("sigue abiero")

	print(contenido)
	print(nombre)
	print(modo)
	print(encoding)
	'''
except:
	print("error al abrir")
finally:
	if archivo:
		#print(archivo)
		archivo.close()
