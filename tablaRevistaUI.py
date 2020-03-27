
from tkinter import*
#from tkinter.ttk import*
import basedatos
#from catalogoUI import CatalogoUI

import tkinter.ttk as ttk
class TablaRevistaUI():

    def __init__(self, estructuraDatos):
        '''@param estructuraDatos Contendra la informacion para representarla en la Tabla
        Deben de ser objetos en la estructura de datos solamente de tipo Libro
        '''
        self.raiz = Tk()
        self.raiz.title("Libros")
        self.raiz.geometry("1200x260")
        self.raiz.resizable(0,False)
        self.frame1 = Frame(self.raiz)
        self.frame1.pack()
        lb_header = ['Titulo', 'Tipo de revista', 'Entidad', 'Fecha', 'Precio']
        #lb_list = [
        #('Dracula', 'Porrua', 1998, 'Terror', '3Edicion', 315)
        #]
        lb_list = []

        for item in estructuraDatos:
            #precondicion-> Sabemos que atributos hay en un libro
            tupla = []
            tupla.append(item.titulo)
            tupla.append(item.tipoRevista)
            tupla.append(item.entidad)
            tupla.append(item.fecha)
            tupla.append(item.precio)
            lb_list.append(tuple(tupla))



        self.tree = ttk.Treeview(columns = lb_header, show = "headings", selectmode = 'browse')
        #self.tree.grid(in_ = self.frame1)
        self.scroll = Scrollbar(self.raiz, orient = "vertical", command = self.tree.yview)
        self.scroll.pack(side = 'right', fill = Y) #
        self.tree.pack(side='left')
        self.tree.configure(yscrollcommand=self.scroll.set)
        for col in lb_header:
            self.tree.heading(col, text = col)
        for item in lb_list:
            #Debe de ser un tupla, un valor constante
            self.tree.insert('','end', values = item)
        
        #self.regresarBtton = Button(self.frame1, text = "Regresar", command = self.listenerRegresar)
        #self.regresarBtton.pack()
        self.raiz.mainloop()
        pass

    def listenerRegresar(self):
        self.raiz.destroy()
        #CatalogoUI()
        pass
    
    pass