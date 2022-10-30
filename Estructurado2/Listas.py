nombre=['Juan','Karlas','Ricardo','Maria']
#imprime la lista de nombre
print(nombre)

#accede a los elemntos de una lista
print(nombre[0])
print(nombre[1])
#accede alos elementos demanera inversa

print(nombre[-1])
print(nombre[-2])
#imprime un rango
print(nombre[0:2])
#ir al inicio de la lista al indice
print(nombre[:2])
#desde el indice indicado hasta el final 
print(nombre[1:])

nombre[3]='Ivone'
print(nombre)
#iterar nombres
for nombres in nombre:
    print(nombres)

#Preguntar el alrgo de la lista 
print(len(nombre))

#agregar un elemnto 

nombre.append('Lorenzo')
print(nombre)

#insertt u elelemnto en especifico 

nombre.insert(1, 'Oscar')
print(nombre)

nombre.remove('Oscar')
print(nombre)
#remover el ultimo valor agrgado
nombre.pop()
print(nombre)

#elimiar elemento en un indice indicado 

del nombre[0]
print(nombre)

#limpiar la lista

nombre.clear()
print(nombre)

#borar la lista por completo
