from tkinter import*
from registroLibroUI import RegistroLibroUI
from registroRevistaUI import RegistroRevistaUI
from registroAudioLibroUI import RegistroAudioLibroUI
from registroJugueteUI import RegistroJugueteUI

class RegistrosUI():

	def __init__(self):
		self.raiz = Tk()
		self.raiz.title("Registro de productos")
		self.raiz.geometry("450x550")
		self.raiz.resizable(False, False)
		self.frame1 = Frame(self.raiz).pack()
		self.radio = IntVar()
		self.registrosLbel = Label(self.frame1, text = "Registro de productos").pack()
		self.librosRbutton = Radiobutton(self.frame1, text = "1.- Libros", variable = self.radio, value = 1, command = self.listenerSelection).pack(anchor = W)
		self.revistasRbutton = Radiobutton(self.frame1, text = "2.- Revistas", variable = self.radio, value = 2, command = self.listenerSelection).pack(anchor = W)
		self.audioLibrosRbutton = Radiobutton(self.frame1, text = "3.- Audiolibros en CD", variable = self.radio, value = 3, command = self.listenerSelection).pack(anchor = W)
		self.juegosDitacticosRbutton = Radiobutton(self.frame1, text = "4.- Juguetes didacticos", variable = self.radio, value = 4, command = self.listenerSelection).pack(anchor = W)
		self.messageOpcionLbel = Label(self.frame1)#.pack() (1)#Cuando llamas al metodo pack() se cambio a un objeto NoneType y ya no puedes acceder a sus atributos
		self.messageOpcionLbel.pack() #(1)Solucion arreglada poner el pack en otra linea asi puedo configurar sus atributos y no cambia a un objeto NoneType
		self.confirmarBtton = Button(self.frame1, text = "Confirmar", activebackground = "gray", command = self.listenerConfirmar)
		self.confirmarBtton.config(state = "disable")
		self.confirmarBtton.pack() #(2)
		self.raiz.mainloop()
	

	def listenerSelection(self):
		selection = "La opcion seleccionada es: " + str(self.radio.get())
		self.messageOpcionLbel.config(text = selection)
		self.confirmarBtton.config(state = "normal")
		#(1)self.messageOpcionLbel.pack()
		#(2)self.confirmarBtton.pack()
		pass
	def listenerConfirmar(self):
		choice = (self.radio.get())
		#print(type(choice))
		if(choice == 1):
			#Registro de libro
			self.raiz.destroy()
			RegistroLibroUI()
			pass
		elif choice == 2:
			self.raiz.destroy()
			RegistroRevistaUI()
			pass
		elif choice == 3:
			self.raiz.destroy()
			RegistroAudioLibroUI()
			pass
		else:
			self.raiz.destroy()
			RegistroJugueteUI()
			pass
		pass


#RegistrosUI()