def sumar(a = 0, b = 0): # como vimos en los parametros de funciones si en el llamado de la funcion no colocamos los argumentos nos dara un error para evitar esto podemos asignar un valor dentro de los parametros de la funcion para que cuando no se agrege en los argumentos de la funcion use ñps valores por defecto, para dejar valores por defecto simplemente agregamos los datos con igual en las variables que estan en parentesis de la funcion
    return a + b

resultado = sumar(5, 3)
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar()}') # como vemos no pasamos argumentos y no nos da error pero nos da la suma esto es gracias a que en la funcion tenemos valores por defecto y por eso da 0 por que usa esos valores por defecto y suma 0 + 0 ( ya que a = 0 y b = 0 en valores por defecto)

# aunque si dejamos encima del llamado de la funcion el mouse nos mostrara una pista de los tipos de datos que tenemos que pasarle a la funcion y el tipo de dato de retorno, pero esto es una pista no es obligatorio incluso al no ser obligatorio podemos pasarle cualquier tipo de dato, tambien podemos colocarle este tipo de sintaxis que vemos en la pista pero aun colocandolo al ser solo una pista de datos podemos enviarle aun asi cualquier tipo de dato tanto en los argumentos como en el retorno
def sumar2(a: int = 0, b: int = 0) -> int: # como vemos podemos colocar una pista de retorno con el simbolo -> y podemos colocarle cualquiert tipo de dato que queremos que retorne y como vimos anteriormente de las pistas de las variables podemos hacerlo igual en los parametros usando : y cualquier tipo de dato que queremos asignarle perto recuerda esto es una pista por ende python no dara error si pasamos otro tipo de dato, ya que en python los tipos de datos son dinamicos
    return a + b
print(sumar2('1','0'))