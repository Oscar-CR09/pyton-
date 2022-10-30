def imprimirNumeroRecursivo(numero):
    if numero >=1:
        print(numero)
        imprimirNumeroRecursivo(numero-1)
    elif numero==0:
        return
    else:
        print('Valor incorrecto')

imprimirNumeroRecursivo(-2)
