from sqlite3 import connect


class usuario():
    
    numUsuarios=0

    def __init__(self,nombre,contra):
        self.nombre =nombre
        self.contra= contra

        self.conectado =False
        self.intentos =3

        usuario.numUsuarios+=1

    def  conectar (self):
        myContra=input("Ingresa tu contraseña")

        if myContra==self.contra:
            print("Se a conectado con exito")
            self.conectado=True

        else:
            self.intentos-=1
            if self.intentos>0:

                print("Contraseña incorrecta ")
                print("Intentos restantes",self.intentos)
                self.conectar()

            else:
                print("Error, no se pudo iniciar sesion ")
                print("Adios !! ")


    def desconectar(self):
        if self.conectado:
            print("Se cerro sesion con exito")
            self.conectado=False

        else:
            print("Error, no se inicio sesion ")


    def __str__(self):
        if self.conectado:
            connect="Conectado"

        else:
            connect="Desconectado"

        return f"Mi nombre de usuarioes es {self.nombre} y estoy {connect} "

user1 =usuario(input("Ingrese un Nombre: "),input("Ingrese su contraseña: "))
print(user1)

user1.conectar()
print(user1)

user1.desconectar()
print(user1)
