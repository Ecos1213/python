mes = int(input('Proporciona mes del año (1-12): '))
estacion = None # en python podemos declarar una variable como None, esto sirve para indicarle que esta variable no va a contener ningun valor

# esto tiene como beneficion si hacemos la siguiente condicional, verificando si la variable contiene none ejecute algo
# if estacion == None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'

print(f'Para el mes {mes} la estación es: {estacion}')

