class Cubo:
    def __init__(self,ancho,alto,profundo):
        self.ancho=ancho
        self.alto=alto
        self.profundo=profundo

    def volumneCubo(self):
        return self.ancho * self.alto * self.profundo

    #def ingresar(self):
        #ancho=int(input('Ingresa el ancho del cubo a calcular'))
        #alto=int(input('Ingresa el alto del cubo a calcular'))
        #profundo=int(input('Ingresa la profundidad del cubo a calcular'))


ancho=int(input('Ingresa el ancho del cubo a calcular: '))
alto=int(input('Ingresa el alto del cubo a calcular: '))
profundo=int(input('Ingresa la profundidad del cubo a calcular: '))

cubo1=Cubo(ancho, alto, profundo)

print(f'El volumnen del cubo es: {cubo1.volumneCubo()}')
