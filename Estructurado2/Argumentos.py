def SumarValores(*args):
    resultado=0
    for valor in args:
        #resultado =resultado + valor
        resultado+=valor

    #pass
    return resultado

print(SumarValores(3,5,9,5,6))