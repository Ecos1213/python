numero = int(input('Proporciona un valro entre 1 y 3: '))

numeroTexto = ''

if numero == 1:
    #recuerda que si declaramos variable solo dentro del if recuerda el scope esa variable solo funcionara en elif por eso es mejor declarar fuera la variable por seguridad de que no sucede un error por culpa del scope por eso numerotexto la declaramos afuera
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'Numero proporcionado: {numero} - {numeroTexto}')

