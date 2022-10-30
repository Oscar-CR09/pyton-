class Pers:
    contador_persona=0
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona +=1
        return cls.contador_persona

    def __init__(self,nombre,edad):
        # Pers.contador_persona +=1 se creo classmethod para separarlo
        self.ID_persona=Pers.generar_siguiente_valor() #Pers.contador_persona
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return f'Personas [ {self.ID_persona} {self.nombre} {self.edad} ]'

persona1=Pers('Juan', 18)
print(persona1)
persona2=Pers('Karla', 30)
print(persona2)
persona3 = Pers('Eduardo', 25)
print(persona3)
print(f'Valor contador personas : {Pers.contador_persona} ')
Pers.generar_siguiente_valor()
persona4=Pers('Maria',35)
print(persona4 )

