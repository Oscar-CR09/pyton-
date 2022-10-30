def MultiplicarValores(*args):
    resultado=1
    for valor in args:
        #resultado =resultado + valor
        resultado*=valor

    #pass
    return resultado

print(MultiplicarValores(3,5,15))
