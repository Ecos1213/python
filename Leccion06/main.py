"""
Ejercicio: Convertidor de Tempertura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
"""

#Funcion que convierte de celsius a fahrenheit
def convertirAFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32 # como a multiplicacion y la division tienen la misma precedencia de operadores y el codigo se lee de izquierda a derecha primero hara la multiplicacion por eso se peude encerre la division en parentesis para que la haga primero antes de la multiplicacion, pero esto no es necesario ya que el el resultado da el mismo si primero multiplica por 9 y despues divide el resultado por 5 por eso no es necesario el parentesis
    return fahrenheit

#Funcion de fahrenheit a celsius
def convertirACelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 # en este caso colocamos el parentesis la resta por que primero haria la multiplicacion antes que la resta y aqui si cambiaria la operacion si primero hace la multiplicacion antes que la resta por eso los parentesis en la resta
    return celsius

# Realizamos algunas pruebas de conversion
celsius = float(input('Proporcione su valor en celsius: '))
gradosFahrenheit = convertirAFahrenheit(celsius)
# Imprimimos el resultado
print(f'{celsius} C a F: {gradosFahrenheit:.2f}') # en la impresion podemos darle un formato a los float y esto se hace colocando : al lado derecho de la variable tipo de dato float y posteriormente colocamos cuantos digitos queremos que se imprima en este caso es .2f se colca .2 y la f para que sepa que son decimales y la f para que entienda que es flotante y esta es la sintaxis para que entienda que se va aplicar el formato que imprima dos decimales flotantes, recuerda que este formato solo funciona con el print

# Realizamos la prueba de grado fahrenheit a celsius
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
gradosCelsius = convertirACelsius(fahrenheit)
# Imprimimos el resultado
print(f'{fahrenheit} F a C: {gradosCelsius:0.2f}') #el formato de los decimales tambien puede ser 0.2f el 0 hace referencia que no importa la cantidad de digitos que hay a la izquierda, pero que el lado derecho unicamente va a mostrar dos digitos flotantes
