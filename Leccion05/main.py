# coleccion de tipo set, a cambio de la tupla y las listas es que el set no permite un orden y no permite elementos duplicados
# en el set no permite modificar los elementos almacenados, pero es posible agregar mas elementos o eliminarlos
# en los set al no tener un orden cuando mandamos a imprimir estos elementos el orden es completamente aleatorio ya que no tenemos un indice con el cual apoyarnos y/o ordenar estos elementos, asi que por lo tanto un set no mantiene un orden, ademas que no es posible modificar estos elementos una vez que agregamos el elemento al set pero podemos agregar nuevos elementos y eliminarlos, recuerda el set no permite elementos duplicados

# set
planetas = {'Marte', 'Jupiter', 'Venus'} # como vemos para definir un set necesitamos definirlo con llaves {}
print(planetas) # como vemos cada vez que ejecutamos el orden es aleatorio

#el set tiene tambien metodos similares con una tupla y una lista

# len para largo de los elementos (osea la cantidad de elementos que tiene en este caso el set)
print(len(planetas))

# en un set podemos ver si un elemento ya existe
# revisar si un elemento esta presente
# con 'Marte' in planetas verifica si Marte existe en el set de planetas, si existe nos retornara True si no False
print('Marte' in planetas)

# agregar un elemento
planetas.add('Tierra') # con el metodo anidado de los set podemos invocarlo para que nos agrege el elemento y como parametro pasamos el valor a agregar y como en el set no incluye un orden entonces aun agregando este elemento al mostrarlo nos mostrara su orden aleatoriamente
print(planetas)

#no se puede duplicar elementos
planetas.add('Tierra') # como los set no permite duplicar elementos lo que hace python es intetar agregarlo pero como ya existe no lo agrega
print(planetas)

# eliminar elemento
planetas.remove('Tierra') # si necesitamos remover un elemento podemos usar el remove como en las listas este metodo lo que hace es buscar el elemento y si es similar al parametro que pasamos entonces remueve el elemento si no no lo hara
print(planetas)

# si el metodo remove no encuentra el valor nos enviara un error
# eliminar elemento posiblemente arrojando un error
#planetas.remove('Tierra')
#print(planetas)

# hay otra manera de eliminar sin que nos envie un mensaje de error si no encuentra el elemento y es usando el metodo discard funciona igual que remove pero si no encuentra el valor no nos arrojara un error y no eliminara nada si no encuentra el valor
# eliminar elemento sin arrojar error
planetas.discard('Jupiter')
print(planetas)

planetas.discard('Jupiter')
print(planetas)

# como en las listas tambien podemos limpiar por completo un set sin borrarlo de la memoria
planetas.clear()

# tambien podemos eliminar por completo incloso de la memoria como la tupla y listas
del planetas
print(planetas) # nos arroja un error por que ya no podemos acceder al set de planetas ya que se elimino incluso desde la memoria 