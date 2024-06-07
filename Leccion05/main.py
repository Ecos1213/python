# un tupla es inmutable ( no se puede modificar los valores recien agregados) y una lista si es mutable
# una lista tiene un orden y nos permite modificar agregar  e insertar elementos
# las tuplas tienen similitudes con las listas, una tupla sigue guardando el orden de los elementos que se van agregando como la lista pero ya no se puede modificar los elementos de la tupla a diferencia de una tupla ya no podemos ni agregar elementos, modificarlos y tampoco eliminarlos por eso se le conoce como un tipo inmutable

#definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba') # para declara una tupla usamos parentesis () de en vez de corchetes [] que haciamos con las listas y esta tambien respetan el orden la unica diferencia es que son inmutables (ni insertar, ni modificar, ni elminar), esta inmutabilidad sucede cuando declaramos la tupla con sus elementos
# recuerda una tupla se ve igual que una lista solo que las tuplas son inmutables

# las funciones que podemos usar en una tupla tambien son similares

print(frutas) # podemos imprimir la tupla completa como haciamos con el array y nos mostrara la tupla, esta imprimi con parentesis de en vez de corchetes

#saber el largo de la tupla
print(len(frutas)) # como vimos anterior en la lista el metodo len nos devuelve la cantidad de elementos que tiene la tupla

#acceder a un elemento
print(frutas[0]) # para acceder a un valor podemos hacer lo mismos que las listas usando corchetes y el numero del indice podemos acceder a ese valor

# navegacion inversa
print(frutas[-1]) # como vimos en las listas tambien en las tuplas podemos usar numeros negativos y este como en las listas nos dara el ultimo valor si es -1 si es -2 antes del ultimo y asi sucesivamente

# acceder a un rango de valores
print(frutas[0:1]) # como en las listas podemos acceder a un rango de valores que era que comienza desde el indice 0 : 1 tome solo 1 valor de la tupla, osea que solo mostrara el primer valor
# una cosa a tener en cuenta es que cuando accedemos a rango de valores de una tupla y este solo devuelve un solo valor, este para no ser un tipo de dato string y sea una tupla este tiene que contener por lo menos una coma para que determine que es una tupla de lo contrario seria una cadena entre parentesis, por eso si es solo un elemento este ultimo elemento y unico tiene que tener una coma dentro de los parentesis
print(frutas[0:2]) # tomara de 0 a 2 valores osea 0 y 1