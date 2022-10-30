from  Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

#no se puede instanciar una clase abstracta
#figura = FiguraGeometrica()


print('Creacion Objeto cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(lado=5,color='rojo')
cuadrado1.alto=9
cuadrado1.ancho=9
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
#print(cuadrado1.color)
print(f'Calculo area cuadrado {cuadrado1.calcularArea() }')
print(cuadrado1)
#mro Method Resolution order muestra el orden que se manda a llamar en las clases
#print(Cuadrado.mro())

print('Creacion Objeto Rectangulo'.center(50, '-'))
rectangulo1=Rectangulo(ancho=9,alto=8,color='verde')
rectangulo1.ancho=15
print(f'Calculo de area rectangulo {rectangulo1.calcularArea()}')
print(rectangulo1)

print(Cuadrado.mro())