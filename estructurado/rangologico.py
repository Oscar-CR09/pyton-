valor=int(input('Escribe el valor: '))
valorMinimo=0
valorMaximo=5
dentroRango= (valor>=valorMinimo) and (valor<=valorMaximo)

if dentroRango:
    print(f'el valor {valor} esta dentro de rango')

else:
    print(f'El valor {valor} esta fuera de rango')

    