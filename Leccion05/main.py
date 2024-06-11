# los diccionarios son colecciones de datos organizados, a diferencia de los otros eston llevan una llave y esa llave tiene un valor, tal cual como se maneja los diccionarios en la vida real

#dict, los diccionarios tambien usan llaves como los set, pero recuerda a diferencia este tendra una llave y despues el dato, la llave se pueden usar cuarlquier tipo inmutable (int, float, bool, str, etc)
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