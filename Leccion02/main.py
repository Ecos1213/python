print("Proporcione los siguientes datos del libro:")
nombre = input("Proporciona el nombre: ")
codigo = int(input ("Proporciona el ID: "))
precio = float(input("Proporcine el precio: "))
#envioGratis = bool(input("Indica si el envio es gratuito (True/False): ")) # en python no podemos usar el metodo bool por que los valores que lleguen como cadena osea cualquier character que llegue lo convertira como true y si es un valor vacio lo convertira como false
envioGratis = input("Indica si el envio es gratuito (True/False): ")

#esta es una manera en que nos que llegue como True en cadena pasarlo a booleano, por que el bool siempre tomara true por cualquier caracter y si esta vacio sera false
if envioGratis == 'True':
    envioGratis = True
elif envioGratis == 'False':
    envioGratis = False
else:
    envioGratis = 'Valor incorrecto, debe escribir True/False'

#print(f'Nombre: {nombre}')
#print(f'Codigo: {codigo}')
#print(f'Precio: {precio}')
#print(f'Envio Gratuito?: {envioGratis}')

# en python si en el print queremos agregar inforamcion en varias lineas dentro del mismo print podemos usar triple comillas simples y asi tomara los tabuladores e incluso los saltos de linea, es una cadena ya con formato como se ve en el siguiente codigo, incluso podemos usar f para interpolacion de datos
print(f'''
    Nombre: {nombre}
    Id: {codigo}
    Precio: {precio}
    Envio Gratiuto? {envioGratis}
''')

