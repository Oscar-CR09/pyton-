from NumerosIdenticosException import NumerosIdenticosExceptiones

resultado=None


try:
    a = int(input('Primer numero: '))
    b = int (input('Segundo numero: '))
    
    raise NumerosIdenticosExceptiones('Numeros identicos')
    
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error {e}, {type(e)}')

except TypeError as e:
    print(f'TypeError - ocurrio un error {e} {type(e)}')

except Exception as e:
    print(f'Excepcion - Ocurrio un error {e} {type(e)}')

else :
    print('Nose arrojo ninguna excepcion')

finally:
    print('Ejecucion del bloque finalizo')

print(f'resultado: {resultado}')
print('Continuacion...')