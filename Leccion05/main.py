ejemplos = ['Juan', 'Karla', 'Ricardo', 'Maria', 0, 200, True] # como en php para definir un array podemos usar [] corchetes y en python se pueden definir arrays de varios tipo de datos ya sea string, int, float, etc y cada valor tiene su indice
# Definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria'] # es buena pratica declarar los arrays en plural
# imprimir la lista de nombres
print(nombres) #en python podemos imprimir un array directamente con el metodo print sin iterar o recorrer el array y el nos imprimira el array incluso con los corchetes

# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])

# tambien podemos acceder a los elementos de una lista con indices negativos, el -1 seria el ultimo valor de la lista, el -2 el siguiente valor y asi sucesivamente
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4])

#imprimir un rango
print(nombres[0:2]) # podemos tomar valores de un array desde un indice hasta un rango que queremos tomar esto quiere decir que tome el valor de 0 : 2 (este dos no es un indice realmente si no mas bien le estamos diciendo que tome 2 valores) y de ahi tome dos valores osea que toamara el 0 y el 1 por eso imprime los dos primeros valores

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) # en este caso le estamos diciendo que incluyame el primer indice de la lista que existe (por eso dejamos vacio el primer valor) : 3 y de ahi tome 3 valores incluyendo el primer valor del primer indice de la lista, osea que tomara el valor del indice 0,1,2

#desde el indice indicado hasta el final
print(nombres[1:]) # en este caso le estamos diciendo que incluyame el indice 1 : hasta el ultimo valor del indice que existe ( por eso dejamos el ultimo valor vacio para que python interprete que es el ultimo valor de la lista) osea que tomara el indice 1,2,3 (ya que el indice 3 es el ultimo valor por ende tomara todos los valores si dejamos el ultimo valor vacio)

#cambiar un valor
# si queremos modificar un valor de un array podemos hacerlo incluso como se hace en php y es de la siguiente forma
nombres[3] = 'Ivone'
print(nombres)

#iterar una lista
for nombre in nombres: # si queremos iterar una lista con el for podemos hacerlo y simplemente colocamos el array despues del in y el automaticamente recorrera (ya que es un foreach) cada valor y lo pondra en la primera variable que en este caso es nombre
    print(nombre)
else:
    print('No existe mas nombres en la lista')

# preguntar el largo de una lista
print(len(nombres)) # con el metodo len nos retorna la cantidad de elementos que tiene una lista y como parametro pasamos la lista

# agrega un elemeto a la lista
nombres.append('Lorenzo') # append agrega un elemento a la lista y como vemos usamos la variable donde contiene el array y usamos el metodo de esta misma variable para que agrege en este array con el append el elemento que agregamos como parametro al metodo y este agragara un nuevo elemento al final de la lista
print(nombres)

# insertar un elemento en un indice especifico
nombres.insert(1, 'Octavio') # insert agrega un elemento a la lista en indice especifico, tiene dos parametros primero es el indice donde queremos que lo inserta para despues correr a los otros valores al lado derecho y despues el elemento a insertar y como el append este metodo se usa de la misma manera usando el array con un punto para invocar el metodo
print(nombres)

# remover un elemento
nombres.remove('Octavio') # el metodo remove remueve un elemento, lo que hace es buscar en el array el valor que agregamos como parametro si encuentra un elemento similar al parametro que agregamos lo remueve y este tambien se invoca a traves del tipo de dato array
print(nombres)

# remover el ultimo valor agregado de la lista
# si dejamos el cursos en el metodo y le damos ctrl + espacio nos aparecera una ventana al darle a los 3 puntos podemos elegir quick documentation y nos muestra que hace el metodo
nombres.pop() # el metodo pop elimina el ultimo elemento de la lista y regresa el indice indicado, no necesita argumentos y se invoca tambin atravez del array
print(nombres)

# eliminar un elemento segun el indice indicado
del nombres[0] # para eliminar un elemento segun el indice indicado usamos al principio la palabra del y despues colocamos el array y entre corchetas el indice a eliminar
print(nombres)

# si queremos limpiar todos los elementos de la lista
nombres.clear() # el metodo clear eliminara todos los elementos de la lista
print(nombres) # mostrara el array vacio por que aun esta definido en la memoria y es un array vacio

#el problema es que clear no elimina de la memoria nuestra lista, pero podemos hacer lo siguiente para borrar nuestra lista de la memoria
del nombres # con la palbra del y despues el array borrara la lista por completo incluso de la memoria
print(nombres) # como borramos la lista de la memoria nos aparecera un error ya que no esta definido