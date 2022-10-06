import tkinter as tk
from tkinter import ttk

from model.pelicula import borrar_tabla, crear_tabla
from mysqlx import Column, Row


def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu,width=300,height=300)
    
    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label="INICIO",menu=menu_inicio)
    
    menu_inicio.add_command(label='Crear Reistro en BD',command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Reistro en BD',command=borrar_tabla)
    menu_inicio.add_command(label='Salir',command=root.destroy)

    barra_menu.add_cascade(label="CONSULTAS")
    barra_menu.add_cascade(label="CONFIGURACION")
    barra_menu.add_cascade(label="AYUDA")


class Frame(tk.Frame):

    def __init__(self,root=None):
        super().__init__(root, width=480, height=320 )
        self.root=root
        self.pack() 
        #self.config(bg="orange")

        self.campos_peliculas()
        self.desabilitar_campos()  
        self.tabla_peliculas()      

    def campos_peliculas(self):
        #label
        self.label_nombre=tk.Label(self,text='Nombre:')
        self.label_nombre.config(font=('Arial','12','bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text='Genero:')
        self.label_genero.config(font=('Arial', '12', 'bold'))
        self.label_genero.grid(row=2, column=0,padx=10,pady=10)

        #campos de entrada

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12,'bold'))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self,textvariable=self.mi_genero)
        self.entry_genero.config(
            width=50, font=('Arial', 12, 'bold'))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)


        #botones
        self.boton_insertar=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_insertar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#010101', bg='#36D119', cursor='hand2', activebackground='#35BD6f')
        self.boton_insertar.grid(row=3,column=0,padx=10,pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar",command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#010101', bg='#319A9B', cursor='hand2', activebackground='#35BD6f')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar",command=self.desabilitar_campos)
        self.boton_cancelar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#010101', bg='#AF0A0A', cursor='hand2', activebackground='#35BD6f')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)


    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')


    def desabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disable')
        self.entry_genero.config(state='disable')

        self.boton_guardar.config(state='disable')
        self.boton_cancelar.config(state='disable')

    def guardar_datos(self):
        self.desabilitar_campos()



    def tabla_peliculas(self):
        self.tabla= ttk.Treeview(self,column=('Nombre','Genero'))
        self.tabla.grid(row=4,column=0,columnspan=4)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2',text='GENERO')

        self.tabla.insert('',0,text='1',values=('los Vengadores','Accion'))


        #boton editar
        self.boton_editar = tk.Button(
            self, text="Editar")
        self.boton_editar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#010101', bg='#36D119', cursor='hand2', activebackground='#35BD6f')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)


        #boton eliminar
        self.boton_eliminar = tk.Button(self, text="Eliminar")
        self.boton_eliminar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#010101', bg='#AF0A0A', cursor='hand2', activebackground='#35BD6f')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)






