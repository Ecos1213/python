"""
Ejercicio: Calculadora de impuestos
crear una funcion para calcular el total de un pago inlcuyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuetos * (impuesto/100)
"""

#Funcion que calcula el total de un pago incluyendo el impuesto
def calcularTotalPago(pagoSinImpuesto, impuesto = 0):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal

# Ejecutamos funcion
pagoSinImpuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto: "))
pagoConImpuesto = calcularTotalPago(pagoSinImpuesto, impuesto)
print(f"""Pago con impuesto: 
{pagoConImpuesto}""")