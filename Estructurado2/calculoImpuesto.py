def CaculoImpuesto(pagoSI,impuesto):
    pagoTotal=pagoSI+pagoSI*(impuesto/100)
    return pagoTotal

pagoSI=float(input('Proporcione el pago sin impuesto: '))
impuesto=float(input('Proporciona el monto del impuesto: '))

pagoConImpuesto=CaculoImpuesto(pagoSI, impuesto)
print(f'Pago con impuesto : {pagoConImpuesto}')