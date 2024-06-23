# una funcion recursiva es una funcion que se llama asi misma para completar una cierta tarea como por ejemplo, el ejemplo clasico factorial de un numero
"""
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2
5! = 5 * 4 * 6
5! = 5 * 24
5! = 120

"""
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1) # como vemos podemos utilizar la misma funcion dentro de ella y esto lo hacemos para hacer el factorial multiplicando el numero por el factorial del numero - 1 y esto se ejecutara hasta que el valor de numero sea 1 osea que tomara lo siguiente: si colocamos 5 entonces sera 5 * (5-1)(ejecuta esta funcion) 4 * (4-1)(ejecuta esta funcion) 3 * (3-1)(ejecuta esta funcion) 2 * (2-1)(ejecuta esta funcion) 1 como es uno retornara 1 y al ejecutar cada funcion queda asi: 5 * 4 * 3 * 2 * 1 como un factorial
        # lo que hara python con la funcion interna como no sabe la respuesta al principio quedara en espera y cuando termine ejecutara su operacion, el modo debug podemos ver al lado izquierda en el MainThread cada espera de estas funciones

numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')