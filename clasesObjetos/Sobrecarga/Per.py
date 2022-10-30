class Per:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad  

    def __add__(self,other):
        return f' {self.nombre} {other.nombre} '

    def  __sub__(self,other):
        return self.edad - other.edad


per1=Per('Juan',28)
per2=Per('Carlos',50)

print(per1 + per2)
print(per1 - per2)
