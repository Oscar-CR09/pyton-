#definir una tupla
frutas=('Naranja','platano','Guayaba')
print(frutas)
#saber el largo 
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder de rango 
print(frutas[0:1])

#recorre elementos

for fruta in frutas:
    print(fruta)#print(fruta,end='')


#cambiar valor tupla no se puede
#comvercion de tuplas a listas lista a Tuplas

frutaLista=list(frutas)
frutaLista[0]='Pera'

frutas=tuple(frutaLista)
print(frutas)