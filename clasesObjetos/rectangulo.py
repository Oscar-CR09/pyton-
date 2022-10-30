class rectangulo:
    def __init__(self,base,altura):
        self.base =base
        self.altura=altura

    def area(self):
        return self.base * self.altura

    #def llamar(self):
        #int(input(base))
        #int(input(altura))


base=int(input('Proporciona la base: '))
altura=int(input('Proporciona la altura: '))

rectangulo1=rectangulo(base, altura)

print(f'Area del rectangulo: {rectangulo1.area()}')

