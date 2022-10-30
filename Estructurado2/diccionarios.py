#diccionario (key , value)

diccionario={
    'IDE': 'Integrate Development Environment',
    'OOP': 'Object Orient Programming',
    'DBMS': 'DMBD'
}

print(diccionario)

print(len(diccionario))
#acceder un elemento
print(diccionario['IDE'])
#otra forma de reuperar otro elemento
print(diccionario.get('OOP'))
#modificar elemento

diccionario['IDE']='integrate development environment'
print(diccionario)

for termino ,valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)


#comprovar existencia de un elemento

print('IDE'in diccionario)

#agregar elememento
diccionario['PK']='Primery Key'
print(diccionario)

#remover un elemento

diccionario.pop('DBMS')
print(diccionario)

#limpiar
diccionario.clear()
print()


#eliminar diccionario
#del diccionario
#print diccionario