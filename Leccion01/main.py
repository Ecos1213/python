x = 10  #las variables siempre generan una posicion de memoria haste cuenta que por cada informacion de la variable queda en una casilla de memoria y esta tiene un identifcador unico y la variable apunta a este identificador de memoria
y = 2
z = x + y
print(x)
print(y)
print(z)
print(id(x))  #usamos el metodo id y pasamos como argumento la variable para saber donde esta la direccion de memoria de los valores(literales) podemos usar la funcion id para que nos muestre el identificador unico de la variable que pasemos como parametro, cada vez que ejecutamos nuestro programa es posible que esta apunte a otra direccion de memoria ya que esta se mueve to:do el tiempo por eso siempre no obtendremos los mismos valores
print(id(y))  #recuerda las direcciones de memorias son hexadecimales, a esto se le llama referencia de memoria y cada vez que ejecuta nuestro programa o termina nuestro programa y vuelve a ejecutar cambia esta referencia, esto es debido a que cada vez que termina nuestro programa elimina nuestros valores en la memoria y al volver a ejecutarlo vuelve a crear estos valores con sus nuevas referencias
print(id(z))


