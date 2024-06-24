"""
Imprimir numeros de 5 a 1 de manera descendete usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1
en caso de pasar el valor de 3, debe imprimir:
3
2
1

si se pasan valores negativos no imprime nada
"""

def imprimirNumeroRecursivo(numero):
    if numero >= 1:
        print(numero)
        return imprimirNumeroRecursivo(numero - 1)
    if numero == 0:
        return # en python podemos dejar un return vacio y no retornara nada y termina la funcion pero en este caso al ser una funcion recursiva termina la funcion para que las otras se ejecuten hasta terminar de ejecutar todas
    elif numero <= 0:
        print('Valor incorrecto...')

imprimirNumeroRecursivo(5)
imprimirNumeroRecursivo(3)
imprimirNumeroRecursivo(-3)
