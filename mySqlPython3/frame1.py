from distutils.command.config import config
from struct import pack
from textwrap import fill
from tkinter import *

ventana = Tk()
ventana.title("LOGIN USUARIO")
ventana.geometry("1100x500")

frame1=Frame(ventana,bg="blue")
frame1.pack(expand=True,fill='both')

frame2 = Frame(ventana, bg="yellow")
frame2.pack(expand=True, fill='both')
frame2.config(cursor='heart')

redbutton=Button(frame1,text="red",fg="red")
grenbutton=Button(frame1,text="green",fg="green")
bluebutton = Button(frame1, text="blue", fg="blue")

redbutton.place(relx=.05, rely=.05, relwidth=.25,relheight=.9)
grenbutton.place(relx=.35, rely=.05, relwidth=.25, relheight=.9)
bluebutton.place(relx=.65, rely=.05, relwidth=.25, relheight=.9)

blackbutton=Button(frame2,text="Black",fg="Black")
blackbutton.pack()


ventana.mainloop()