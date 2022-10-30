from teclado import Teclado
from raton import Raton
from monitor import Monitor


class Computadora:
    contadorComputadora=0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contadorComputadora =+ 1
        self._idComputadora=Computadora.contadorComputadora
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton



        def __str__(self):
            return f'''
            
            ID: {self._idComputadora} Nombre: {self._nombre} 
            Monitor: {self._monitor} 
            Teclado: {self._teclado}
            Raton: {self._raton}
             
            '''

if __name__=='__main__':
    teclado1 =Teclado('HP', 'USB')
    raton1=Raton('HP', 'USB')   
    monitor1=Monitor('HP', '15')
    computadora1=Computadora('HP',monitor1,teclado1,raton1)

    print(computadora1)
