
class Orden:
    contadorOrden=0
    def __init__(self,computadoras):
        Orden.contadorOrden +=1
        self._idOrden=Orden.contadorOrden
        self._computadoras=computadoras

    def agregarComputadoras(self,computadora):
        self._computadoras.append(computadora)


    def __str__(self):
        computadoras_str=''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        
        return f'''
        Orden: {self._idOrden}
        Computadoras: {computadoras_str}

        '''


