from tkinter import*
from tkinter import messagebox;
from juguete import Juguete

class RegistroJugueteUI():
	def __init__(self):
		self.raiz = Tk();
		self.raiz.title("Registro de Juguetes")
		self.raiz.geometry("450x550")
		self.nombre = StringVar()
		self.material = StringVar()
		self.precio = StringVar()
		self.frame1 = Frame(self.raiz).pack()
		self.registroL = Label(self.frame1, text = "Registro de juguetes").pack()
		self.nombreL = Label(self.frame1, text = "Nombre del juguete").pack()
		self.nombreEtry = Entry(self.frame1, textvariable = self.nombre).pack()
		self.materialL = Label(self.frame1, text = "Material").pack()
		self.materialEtry = Entry(self.frame1, textvariable = self.material).pack()
		self.precioL = Label(self.frame1, text = "Precio").pack()
		self.precioEtry = Entry(self.frame1, textvariable = self.precio).pack()
		self.registrarBton = Button(self.frame1, text = "Registro", command = self.listenerRegistro).pack()
		self.raiz.mainloop()
	pass

	def listenerRegistro(self):
		if not self.estan_camposCorrectos():
			messagebox.showerror("error","Debe de rellenar todos los campos");
		else:
			toy = Juguete(self.nombre.get(), self.material.get(), self.precio.get())
			try:
				archivo = open("baseDatosJuguetes.txt","a+")
				archivo.write(str(toy))
				archivo.write("\n")
				#Si no esta repetido mandar mensaeje que registro el libro correctamente
				messagebox.showinfo("information","Se ha registrado el libro correctamente"); 
			except FileNotFoundError:
				print("Archivo no encontrado")

	def estan_camposCorrectos(self):
		if(self.nombre.get() == "" or self.material.get() == "" or self.precio.get() == "" ):
			return False;
		return True;

	pass
#RegistroJugueteUI()