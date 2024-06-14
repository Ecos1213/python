#miFuncion() # esto nos aparecera un erorr de miFuncion no esta definida por que primero definimos y despues hacemos la llamada
# las funcioners en python al principio tenemos que colocar la palabra def y despues el nombre de la funcion que queremos colocarle, podemos usar camelCase o serpent case (serpent case es que cada palabra se separa con un _ ejemplo:funcion_pyhthon)
def miFuncion(): # despues de usar def para crear una funcion y el nombre de la funcion tenemos que colocar tambien parentesis y en estos parentesis podemos asignar parametros o argumentos y al final usamos los : como lo haciamos con el if, else, elif o ciclos
    print('Saludos desde mi funcion') # recuerda que todas las lineas que esten identada estaran en nivel de la funcion hasta que una de estas lineas deje de estarlo, ahi se acabara la identacion

miFuncion() # para que se ejecute la funcion con sus respectivos codigo o bloques de codigo necesitamos llamar la funcion asi como todos los lenguajes de programacion
# la ventaja de una funcion es poder reutilizarla las veces que sea necesario
miFuncion()
miFuncion()

# pero recuerda esto no es como javascript ya que en python no podemos llamar la funcion y despues definirla, primero tenemos que definirla despues de su definicion podemos escribir en la siguiente lineas de codigo el llamado de esta, si la llamamos antes de su definicion nos aparecera un error
# mas adelante veremos los modulos en el cual para poder utilizar una funcion tambien podemos importarla asi que si esta funcion se define en otro archivo, en otro modulo, asi que simplmente con importarla vamos a poder utilizarla, sin embargo primero tendriamos que importar la funcion y despues utilizarla