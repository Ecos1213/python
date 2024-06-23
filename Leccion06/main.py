"""
Crear una funcion para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la multiplicacion de todos los valores pasados como argumentos
"""

# Definicion de la funcion para multiplicar valores
def multiplicarValores(*args):
    resultado = 1
    for numero in args:
        resultado *= numero # resultado = resultado * numero
    return resultado

# Llamada de la funcion
print("el total es: ", multiplicarValores(3,5,15))

