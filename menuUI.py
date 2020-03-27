
from tkinter import*
from catalogoUI import CatalogoUI
from registrosUI import RegistrosUI

class MenuUI():

	def __init__(self):
		self.raiz = Tk()
		self.raiz.title("Menu")
		self.raiz.geometry("450x550")
		self.raiz.resizable(False, False)
		self.frame1 = Frame(self.raiz).pack();
		self.tituloLbel = Label(self.frame1, text = "Menu").pack()
		self.revisar_catalogoBtton = Button(self.frame1, text ="Revisar catalogo", command = self.listenerRevisarCatalogo).pack()
		self.registroBtton = Button(self.frame1, text = "Registrar producto", command = self.listenerRegistros).pack()
		self.raiz.mainloop()
		pass

	def listenerRevisarCatalogo(self):
		self.raiz.destroy()
		#Instacion la clase interfaz catalagoUI
		#raiz = Tk()
		#catalogoUI = CatalogoUI(raiz)
		catalogoUI = CatalogoUI()
		#raiz.mainloop()
		pass

	def listenerRegistros(self):
		#Menu de registros
		self.raiz.destroy()
		menuRegistros = RegistrosUI()
		pass


	pass



menu = MenuUI()
