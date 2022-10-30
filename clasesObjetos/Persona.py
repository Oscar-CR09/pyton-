class Persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre  # self._nombre= nombre un guion es para no modificar
        self._apellido=apellido
        self._edad=edad
    #self.__nombre= nombre doble guion es para restringir la modificacion del atributo
    @property  #decorador para llamar un mtodo indirecta encapsular
    def nombre(self):
        print('llamando al metodo get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        print('llamando al metodo set nombre')
        self._nombre=nombre

    @property #encapsular
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad=edad

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')


if __name__ == '__main__':
    persona1=Persona('Juan','Perez',28)
    #print(persona1.nombre)
    persona1.nombre='Juan Carlos'
    persona1.apellido='Lara'
    persona1.edad=30
    persona1.mostrarDetalle()

    print(__name__)


# get=obtener/recuperar de los atributos
# set=colocar/modificar de los atributos  setter
#persona1._nombre='Juan Carlos'
#persona1.mostrarDetalle()


"""
class Persona:
    def __init__(self,nombre,apellido,edad,*args,**kwargs):
        self.nombre= nombre
        self.apellido=apellido
        self.edad=edad
        self.args=args #argumentos
        self.kwargs=kwargs #diccionarios

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')


persona1=Persona('Juan','Perez',28,'55525256',2,3,4,5,m='manzana',p='pera')
persona1.mostrarDetalle()

#persona1.telefono='55441122'
#print(persona1.telefono)
#print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad} ')
#Persona.mostrarDetalle(persona1)

persona2=Persona('Karla','Gomez',30)
persona2.mostrarDetalle()


#print(f'Objeto Perosna 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


"""