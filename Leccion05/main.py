# los diccionarios son colecciones de datos organizados, a diferencia de los otros estas llevan una llave y esa llave tiene un valor, tal cual como se maneja los diccionarios en la vida real

#dict, los diccionarios tambien son como los set, pero recuerda a diferencia este tendra una llave y despues el dato, la llave se pueden usar cuarlquier tipo inmutable (int, float, bool, str, etc)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object oriented programming',
    'DBMS': 'Database Management System'
}

print(diccionario) # como vemos primero imprimira la llave y despues el dato y asi sucesivamente por cada valor

# como los set, tuplas y listas podemos usar el metodo len y despues el argumento que en este caso seria nuestro diccionario de datos para saber la cantidad de elementos que tiene
print(len(diccionario)) # como vemos nos retornara que contiene 3 valores ya que cuenta es cada valor y llaves juntas osea que son 3 en total

# un diccionario se parece un poco a un set por que los diccionarios no tienen indices pero si tienen un orden osea que asi como lo agregemos asi estara ordenado

#acceder a un elemento tenemos que proporcionar la llave(key)
print(diccionario['IDE']) # para acceder al valor de un diccionario tenemos que colocar entre corchetes la llave que contanega el valor que queremos para que nos de su valor

# hay otra forma de acceder a una llave y es usando el metodo anidado get y pasando como parametro la key asociado al valor que queremos mostrar
print(diccionario.get('OOP'))

# como las listas tambien podemos modificar los elementos como se hace en una lista
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

for termino, valor in diccionario.items(): # podemos imprimir tanto la key y el valor de la key con el for(foreach) de python primero tenemos que colocar un metodo anidado llamado items que viene del diccionario, este nos retornara tanto la key como el valor por separado y el for o foreach lo toma y ahi simplemente colocando dos variables que contenga primero el termino y despues el valor ya nos lo mostrara
    print(termino, valor)

# tambien podemos recuperar solo las keys(terminos)
for termino in diccionario.keys(): # si queremos mostrar solo los terminos tambien podemos hacerlo y es colocando el metodo anidado del diccionario llamado keys y este nos retornara solo los terminos y ya con el foreach solo tomamos la variable de terminos y la imrpimos en el foreach
    print(termino)

for termino in diccionario:  # tambien hay otra manera de imprimir terminos y es solo imprimiendo la viarble sin ningun metodo en el diciconario
    print(termino)

# tambien podemos solo mostrar los valores del diciconario
for valor in diccionario.values(): # utilizando el metodo aninado values del diccionario nos pasara solo los valores y el foreach lo recorrera y los pondra en la variable para despues imprimirlo
    print(valor)

# comprobar existensia de algun elemento
print('IDE' in diccionario) # asi como los set podemos ver si existe la key dentro de diccionario usando 'valor' in diccionario y este nos retornara True si existe y False si no

print('IDe' in diccionario) # recuerda que debemos respectar mayusculas y minusculas asi que esto dara False por que no lo encotrara y esto tambien aplica para los set

# agregar un elemento
diccionario['PK'] = 'Primary Key' # como vemos asi podemos agregar una key con un valor en el diccionario y es similar a PHP, la unica diferencia es que no es posible agregar llaves duplicadas, si agregamos una llave existente sobreescribe la llave con el nuevo valor
print(diccionario)

# remover un elemento
diccionario.pop('DBMS') # con el metodo anidado del diccionaro llamada pop podemos remover el elemento y la key. lo que tenemos que hacer es pasar como argumento la key a remover y el metodo se encargara de buscar e eliminar tanto la key como el valor
print(diccionario)

# eliminar todos los elementos
diccionario.clear() # asi como vimos en las listas y set tambien podemos eliminar todos los elementos con el metodo anidado clear
print(diccionario)

#asi como las listas, set y tuplas tambien podemos eliminar por completo incluso de la memoria ram usando al principio la palabra del y despues el diccionario
del diccionario
print(diccionario) # recuerda que el diccionario al borrarse por completo incluso del cache ya deja de existir por lo tanto si volvemos a imprimir despues de borrar por completo nos dara un error ya que no existe