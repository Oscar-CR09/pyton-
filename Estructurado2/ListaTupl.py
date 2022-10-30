tupla=(13,1,8,3,2,5,8)

#definir lista
lista=[]

#filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

    #imprimir lista 
    
print(lista)
