from dispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contadorTeclado=0

    def __init__(self, marca, tipoEntrada):
        Teclado.contadorTeclado +=1 
        self.idTeclado=Teclado.contadorTeclado
        super().__init__(marca,tipoEntrada)


    def __str__(self):
        return f' ID: {self.idTeclado} Marca: {self._marca} Tipo de entrada: {self._tipoEntrada} '



if __name__ == '__main__':
    teclado1=Teclado('HP', 'USB')
    print(teclado1)

    teclado2=Teclado('Gamer', 'Bluetooth')
    print(teclado2 )

    