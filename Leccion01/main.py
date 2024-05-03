x = 10  #Tipo numeric y es un integer
print(x)
print(type(x))  #el metodo type lo que hace es ver que tipo de dato es el valor de la variable

x = "Hola mundo"  #Tipo sequence type y es un string
print(x)
print(type(x))

x: str = 'Hola mundo'  #Tipo sequence type y es un string, en python podemos apuntar al tipo de dato de una variable esto lo podemos hacer con algo llamado hint que es una pista o indicacion para decirle que es de un tipo de dato, hay que usar : despues de la variable y colocar el tipo de dato que queremos indicarle, el tipo de dato tiene que escribirse de forma corta osea str, int, etc. si colocamos un valor no correspondiente al valor del tipo de dato de la pista no pasara alguin error pero el ide nos recordara resaltando que no es el tipo de dato que esta definido
print(x)
print(type(x))

x = 10.5  #Tipo numeric y es un float
print(x)
print(type(x))

x = True  #Tipo boolean y es un boolean, recuerda no se puede escribir true ni false tiene escribirse la primera en mayuscula si no no lo reconocera True y False
print(x)
print(type(x))

#python es un lenguaje de programacion orientado a objetos por lo tanto los tipos de datos tambien son alamacenados en clases
