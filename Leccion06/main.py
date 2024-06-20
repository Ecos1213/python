"""
Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la suma de todos los valores pasados como arguemntos
"""


# Definimos nuestra funcion para sumar valores
def sumarValores(
        *args):  # se recumenda usar un nombre de verbo, se recomienda usar un verbo y despues especificar que hace el verbo en este caso seria sumar valores el verbo es sumar y especificamos que son los valores a sumar
    # si no tenemos todavia la logica de nuestra funcion podemos usar la palabra reservada pass para que python comprenda que esta funcion no tiene logica osea va a estar vacia, por lo tanto aunque la llamemos python vera que esta vacia y no mostrara un error, pero si escribimos una logica en la funcion y tenemos la palabra reservada pass ejecutara la lgoica con normalidad pero se recomienda por buenas praticas quitarla
    #pass

    #por convecion se recomienda en los argumentos varibles usar la palabra args, es por buenas praticas

    resultado = 0
    # Iteramos cada elemento
    for valor in args: # recuerda aca no se usa *, ya que el asterico se usa dentro del argumento de la funcion, el asterisco se usa como parte de la definicion de la firma de estre metodo, es como la firma para declarar que es un argumento variado mientras que aca usamos es la variable como tal
        resultado += valor # es igual a resultado = resultado + valor
    return resultado


print(sumarValores(3, 5, 9, 4, 6))
