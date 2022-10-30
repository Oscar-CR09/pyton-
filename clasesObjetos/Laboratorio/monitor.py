

class Monitor:

    contadorMonitores=0
    def __init__(self,marca,tamaño):
        Monitor.contadorMonitores +=1
        self._idMonitor = Monitor.contadorMonitores
        self._marca=marca
        self._tamaño=tamaño


    def __str__(self):
        return f'ID : {self._idMonitor}, Marca: {self._marca} Tamaño: {self._tamaño}'


if __name__ == '__main__':
    monitor1=Monitor('HP', '15" ')
    print(monitor1)
    monitor2=Monitor('Acer', '27" ')
    print(monitor2 )
    


