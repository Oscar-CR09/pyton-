#set

planetas = {'Marte','jupiter','venus'}

print(planetas)
#largo

print(len(planetas))

#revisar si un elemento este presente
print('marte'in planetas)

#agregar elementos

planetas.add('Tierra')
print(planetas)
#no se puede agregar elementos duplicados 
#eliminar elememento
planetas.remover('Tierra')
print(planetas)
planetas.discard('Jupiter')
print(planetas)
planetas.clear()
#del planetas eliminar por completo
#  