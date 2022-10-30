class MiClase:
    variable_clase='valor variable clase'

    def __init__(self,variable_instancia):
        self.variable_instancia=variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
    
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_clase()
MiClase.metodo_estatico()
miobjeto1=MiClase('variable_instancia')
miobjeto1.metodo_clase()
miobjeto1.metodo_instancia()





"""

print(MiClase.variable_clase)
miClase=MiClase('valor variable de instancia ')
print(miClase.variable_instancia)
print(miClase.variable_clase)

MiClase.variable_clase2='valor variable clase2'

miClase2=MiClase('otro valor de variable instancia ')
print(miClase2.variable_instancia)

print(miClase.variable_clase2)
print(miClase2.variable_clase2)

"""