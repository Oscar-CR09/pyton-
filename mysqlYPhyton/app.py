from cgitb import text
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.tix import Tree

from conexion import *

ventana = Tk()
ventana.title("Crud MySql Tkinter")
ventana.geometry("1100x500")

db=DataBase() #SE CREO LA CLASE BASE DE DATOS PARA ASIGNARLE bd
modificar=False
Nombre=StringVar()
ApellidoM=StringVar()
ApellidoP=StringVar()
sexo=StringVar()
FechaNacimiento = StringVar()
Direccion=StringVar()
Telefono = StringVar()
Email = StringVar()
Matricula = StringVar()


def usuarioClick(event):
    id = Id_Usuario = tvMensajes.selection()[0]
    if int(Id_Usuario) > 0:
        Nombre.set(tvMensajes.item(id, "values")[1])
        ApellidoM.set(tvMensajes.item(id, "values")[2])
        ApellidoP.set(tvMensajes.item(id, "values")[3])
        sexo.set(tvMensajes.item(id, "values")[4])
        FechaNacimiento.set(tvMensajes.item(id, "values")[5])
        Direccion.set(tvMensajes.item(id, "values")[6])
        Telefono.set(tvMensajes.item(id, "values")[6])
        Email.set(tvMensajes.item(id, "values")[7])
        Matricula.set(tvMensajes.item(id, "values")[8])


cuadro= LabelFrame(ventana, text="Formulario de gestion de datos")
cuadro.place(x=20,y=20,width=1050,height=450)

#label

lblnombre=Label(cuadro,text="NOMBRE").grid(column=0,row=0, padx=5,pady=5)
txtnombre=Entry(cuadro,textvariable=Nombre)
txtnombre.grid(column=1,row=0)

lblAMaterno = Label(cuadro, text="APELLIDO MATERNO").grid(
    column=2, row=0, padx=5, pady=5)
txtAMaterno = Entry(cuadro, textvariable=ApellidoM)
txtAMaterno.grid(column=3, row=0)

lblApaterno = Label(cuadro, text="APELLIDO PATERNO").grid(
    column=0, row=1, padx=5, pady=5)
txtApaterno = Entry(cuadro, textvariable=ApellidoP)
txtApaterno.grid(column=1, row=1)

lblsex = Label(cuadro, text="SEXO").grid(column=2, row=1, padx=5, pady=5)
txtsex = ttk.Combobox(cuadro,values=["M","F"], textvariable=sexo)
txtsex.grid(column=3, row=1)
txtsex.current(0)

lblsex = Label(cuadro, text="FECHA NACIMIENTO").grid(column=0, row=3, padx=5, pady=5)
txtsex = Entry(cuadro, textvariable=FechaNacimiento)
txtsex.grid(column=1, row=3)

lbllugar = Label(cuadro, text="DIRECCION").grid(
    column=0, row=4, padx=5, pady=5)
txtlugar = Entry(cuadro, textvariable=Direccion)
txtlugar.grid(column=1, row=4)

lblTel = Label(cuadro, text="TELEFONO").grid(column=2, row=3, padx=5, pady=5)
txtTel = Entry(cuadro, textvariable=Telefono)
txtTel.grid(column=3, row=3)

lblcorreo = Label(cuadro, text="EMAIL").grid(column=2, row=4, padx=5, pady=5)
txtcorreo = Entry(cuadro, textvariable=Email)
txtcorreo.grid(column=3, row=4)

lblMatr = Label(cuadro, text="MATRICULA").grid(column=0, row=5, padx=5, pady=5)
txtMatr = Entry(cuadro, textvariable=Matricula)
txtMatr.grid(column=1, row=5)

lblMensaje=Label(cuadro, text="MENSAJE",fg="red")
lblMensaje.grid(column=0,row=6,columnspan=4)

# tablas de lista

tvMensajes=ttk.Treeview(cuadro,selectmode=NONE)
tvMensajes.grid(column=0,row=7,columnspan=6,padx=5)
tvMensajes["columns"] = ("ID","Nombre", "ApellidoM", "ApellidoP",
                         "Sexo","FechaNacimiento", "Direccion", "Telefono",
                         "Email", "Matricula")
tvMensajes.column("#0",width=0,stretch=NO)
tvMensajes.column("ID", width=50, anchor=CENTER)
tvMensajes.column("Nombre",width=100,anchor=CENTER)
tvMensajes.column("ApellidoM", width=100, anchor=CENTER)
tvMensajes.column("ApellidoP", width=100, anchor=CENTER)
tvMensajes.column("Sexo",width=50,anchor=CENTER)
tvMensajes.column("FechaNacimiento", width=120, anchor=CENTER)
tvMensajes.column("Direccion", width=150, anchor=CENTER)
tvMensajes.column("Telefono",width=80,anchor=CENTER)
tvMensajes.column("Email", width=180, anchor=CENTER)
tvMensajes.column("Matricula", width=80, anchor=CENTER)
tvMensajes.heading("#0",text="")
tvMensajes.heading("ID", text="ID", anchor=CENTER)
tvMensajes.heading("Nombre", text="Nombre",anchor=CENTER)
tvMensajes.heading("ApellidoM", text="ApellidoM", anchor=CENTER)
tvMensajes.heading("ApellidoP", text="ApellidoP", anchor=CENTER)
tvMensajes.heading("Sexo", text="Sexo",anchor=CENTER)
tvMensajes.heading("FechaNacimiento", text="Fecha Nacimiento", anchor=CENTER)
tvMensajes.heading("Direccion", text="Direccion", anchor=CENTER)
tvMensajes.heading("Telefono", text="Telefono", anchor=CENTER)
tvMensajes.heading("Email", text="Email", anchor=CENTER)
tvMensajes.heading("Matricula", text="Matricula", anchor=CENTER)

tvMensajes.bind("<<TreeviewSelect>>",usuarioClick)
#Botones de acciones 

btnEliminar=Button(cuadro, text="Eliminar", command=lambda:eliminar())
btnEliminar.grid(column=4,row=0)
btnInsertar = Button(cuadro, text="Guardar",command= lambda:insertar())
btnInsertar.grid(column=4, row=3)
btnActualizar = Button(cuadro, text="Seleccionar", command= lambda: actualizar())
btnActualizar.grid(column=4, row=5)

#btnActualizar = Button(cuadro, text="Actualizar", command=lambda: actualizar())
#btnActualizar.grid(column=2, row=6)



#funiones 


def modificarFalse():
    global modificar
    modificar=False
    tvMensajes.config(selectmode=NONE)
    btnInsertar.config(text="Guardar")
    btnActualizar.config(text="Seleccionar")
    btnEliminar.config(state=DISABLED)


def modificarTrue():
    global modificar
    modificar = True
    tvMensajes.config(selectmode=BROWSE)
    btnInsertar.config(text="Insertar")
    btnActualizar.config(text="Actualizar")
    btnEliminar.config(state=NORMAL)

def validar():
    return len(Nombre.get()) and len(ApellidoM.get()) and len(ApellidoP.get()) and len(FechaNacimiento.get()) and len(Direccion.get()) and len(Telefono.get()) and len(Email.get()) and len(Matricula.get())
        

def limpiar():
    Nombre.set("")
    ApellidoM.set("")
    ApellidoP.set("")
    sexo.set("")
    FechaNacimiento.set("")
    Direccion.set("")
    Telefono.set("")
    Email.set("")
    Matricula.set("")

def vaciar_tabla():
    filas=tvMensajes.get_children()
    for fila in filas:
       tvMensajes.delete(fila)
   #pass

def llenar_tabla():
    vaciar_tabla()
    sql= "select * from usuario"
    db.cursor.execute(sql)
    filas= db.cursor.fetchall()
    for fila in filas:
        Id_Usuario = fila[0]
        tvMensajes.insert("", END, Id_Usuario, text=Id_Usuario, values=fila)

def eliminar():
    #pass
    Id_Usuario=tvMensajes.selection()[0]
    if int (Id_Usuario)>0:
        sql = "delete from usuario where Id_Usuario="+Id_Usuario
        db.cursor.execute( sql)
        db.connection.commit()
        tvMensajes.delete(Id_Usuario)
        lblMensaje.config(text= "Se a elimnado el registro correctamente")

    else:
        lblMensaje.config(text="Seleccione un registro para eliminar")

def insertar():
    #pass
    if modificar== False:
        if validar():
            
            val = (Nombre.get(), ApellidoM.get(), ApellidoP.get(),sexo.get(), FechaNacimiento.get(), Direccion.get(), Telefono.get(), Email.get(), Matricula.get())
            sql = "insert into usuario (Nombre, ApellidoM, ApellidoP,Sexo,FechaNacimiento ,Direccion, Telefono,Email, Matricula) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            db.cursor.execute(sql,val)
            db.connection.commit()
            lblMensaje.config(text="Se guardo un registro correctamente",fg="green")
            llenar_tabla()
            limpiar()
        else :
            lblMensaje.config(text="Los campos no deben de estar vacios", fg ="Blue")
    else:
        modificarFalse()


def actualizar():
    if modificar == True:
        if validar():
            
            Id_Usuario=tvMensajes.selection()[0]
            val = (Nombre.get(), ApellidoM.get(), ApellidoP.get(),
                   sexo.get(), FechaNacimiento.get(), Direccion.get(), Telefono.get(), Email.get(), Matricula.get())
            sql = "update usuario set Nombre=%s, ApellidoM=%s, ApellidoP=%s,Sexo=%s,FechaNacimiento=%s,Direccion=%s, Telefono=%s,Email=%s, Matricula=%s where Id_Usuario="+Id_Usuario
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMensaje.config(text="Se actualizo correctamente", fg="green")

            llenar_tabla()
            limpiar()
        else:
            lblMensaje.config(text="Los campos no deben de estar vacios", fg="Blue")
    else:
        modificarTrue()



  # pass



llenar_tabla()
ventana.mainloop()