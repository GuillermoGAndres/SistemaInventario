
from tkinter import*
from tkinter import messagebox;
from libro import Libro

class RegistroLibroUI():

	def __init__(self):
		self.raiz = Tk();
		self.raiz.title("Registro de libros")
		self.raiz.geometry("450x550")
		self.titulo = StringVar()
		self.editorial = StringVar()
		self.anioPublicacion = StringVar()
		self.genero = StringVar()
		self.edicion = StringVar()
		self.precio = StringVar()
		self.frame1 = Frame(self.raiz).pack()
		self.registroL = Label(self.frame1, text = "Registro de libro").pack()
		self.tituloL = Label(self.frame1, text = "Titulo").pack()
		self.tituloEtry = Entry(self.frame1, textvariable = self.titulo).pack()
		self.editorialL = Label(self.frame1, text = "Editorial").pack()
		self.editorialEtry = Entry(self.frame1, textvariable = self.editorial).pack()
		self.anioPublicacionL = Label(self.frame1, text = "Año de publicacion").pack()
		self.anioPublicacionEtry = Entry(self.frame1, textvariable = self.anioPublicacion).pack()
		self.generoL = Label(self.frame1, text = "Genero").pack();
		self.generoEtry = Entry(self.frame1, textvariable = self.genero).pack()
		self.edicionL = Label(self.frame1, text = "Edicion").pack()
		self.edicionEtry = Entry(self.frame1, textvariable = self.edicion).pack()
		self.precioL = Label(self.frame1, text = "Precio").pack()
		self.precioEtry = Entry(self.frame1, textvariable = self.precio).pack()
		self.registrarBton = Button(self.frame1, text = "Registro", command = self.listenerRegistro).pack()
		self.raiz.mainloop()
		pass

	def listenerRegistro(self):
		if not self.estan_camposCorrectos():
			messagebox.showerror("error","Debe de rellenar todos los campos");
		else:
			new_book = Libro(self.titulo.get(), self.editorial.get(), self.anioPublicacion.get(), self.genero.get(), self.edicion.get(), self.precio.get())
			#print(new_book)
			try:
				archivo = open("baseDatosLibros.txt","a+")
				archivo.write(str(new_book))
				archivo.write("\n")
				#Si no esta repetido mandar mensaeje que registro el libro correctamente
				messagebox.showinfo("information","Se ha registrado el libro correctamente"); 
			except FileNotFoundError:
				print("Archivo no encontrado")

	def estan_camposCorrectos(self):
		if(self.titulo.get() == "" or self.editorial.get() == "" or self.anioPublicacion.get() == "" or self.genero.get() == "" or self.edicion.get() == "" or self.precio == ""):
			return False;
		return True;

	pass

