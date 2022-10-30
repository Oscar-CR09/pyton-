def gradosCelsiusF(celsius):
    return celsius * 9/5+32

def gradosFCelsius(Fa):
    return (fa-32)*5 /9

celsius=float(input('Proporcione su valor en celsius: '))
resultado=gradosCelsiusF(celsius)

print(f' {celsius} C a F : {resultado :.2f}')

fa=float(input('Proporcione su valor en farenheit: '))
resultado=gradosFCelsius(fa)

print(f'{fa} F a C: {resultado :0.2f}')