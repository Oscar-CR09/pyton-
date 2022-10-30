from Producto import Producto 


class Orden:
    contador_ordenes=0

    def __init__(self,productos):
        Orden.contador_ordenes +=1 
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos) 

    def agregar_producto(self,producto):
        self._productos.append(producto)


    def calcular_total(self):
        total=0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str= ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, \nProductos: {productos_str} '


if __name__ == '__main__':
    producto1 = Producto('camisa', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1,producto2]
    
    orden1 = Orden(productos1)
    print(orden1)

    orden2=Orden(productos1)
    print(orden2)

