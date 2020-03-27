from tkinter import*
from tkinter import messagebox;
from revista import Revista
class RegistroRevistaUI():

	def __init__(self):
		self.raiz = Tk();
		self.raiz.title("Registro de revista")
		self.raiz.geometry("450x550")
		self.titulo = StringVar()
		self.tipoRevista = StringVar()
		self.entidad = StringVar()
		self.fecha = StringVar()
		self.precio = StringVar()
		self.frame1 = Frame(self.raiz).pack()
		self.registroL = Label(self.frame1, text = "Registro de revistas").pack()
		self.tituloL = Label(self.frame1, text = "Titulo").pack()
		self.tituloEtry = Entry(self.frame1, textvariable = self.titulo).pack()
		self.tipoRevistaL = Label(self.frame1, text = "Tipo Revista").pack()
		self.tipoRevistaEtry = Entry(self.frame1, textvariable = self.tipoRevista).pack()
		self.entidadL = Label(self.frame1, text = "Entidad").pack()
		self.entidadEtry = Entry(self.frame1, textvariable = self.entidad).pack()
		self.fechaL = Label(self.frame1, text = "Fecha").pack();
		self.fechaEtry = Entry(self.frame1, textvariable = self.fecha).pack()
		self.precioL = Label(self.frame1, text = "Precio").pack()
		self.precioEtry = Entry(self.frame1, textvariable = self.precio).pack()

		self.registrarBton = Button(self.frame1, text = "Registro", command = self.listenerRegistro).pack()
		self.raiz.mainloop()
		pass

	def listenerRegistro(self):
		if not self.estan_camposCorrectos():
			messagebox.showerror("error","Debe de rellenar todos los campos");
		else:
			magazine = Revista(self.titulo.get(), self.tipoRevista.get(), self.entidad.get(), self.fecha.get(), self.precio.get())
			
			try:
				archivo = open("baseDatosRevista.txt","a+")
				archivo.write(str(magazine))
				archivo.write("\n")
				#Si no esta repetido mandar mensaeje que registro el libro correctamente
				messagebox.showinfo("information","Se ha registrado el libro correctamente"); 
			except FileNotFoundError:
				print("Archivo no encontrado")

	def estan_camposCorrectos(self):
		if(self.titulo.get() == "" or self.tipoRevista.get() == "" or self.entidad.get() == "" or self.fecha.get() == "" or self.precio == ""):
			return False;
		return True;

	pass

#RegistroRevistaUI()