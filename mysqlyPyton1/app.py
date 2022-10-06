#python -m venv env
#
#pip list
#python -m pip install --upgrade pip   ---> actualizar
#python  -m pip install --upgrade pip
#pip install pylint
#pip install autopep8
#paquetes externos

import tkinter as tk

from client.gui_app import Frame, barra_menu


def main ():
    root = tk.Tk()
    root.title('Catalogo de peliculas')
    #root.iconbitmap('imag/logo.ico') #cambiar logo 
    root.resizable(0,0)#modificacion de ventanas
    #tk.Frame=tk.Frame(root) #para tomar tamaño de frame
    #tk.Frame.pack() #asignar tamaño 
    #tk.Frame.config(width=480,height=320, bg="orange")

    barra_menu( root)
    app=Frame(root=root)

    
    root.mainloop()


if __name__== '__main__':
    main()