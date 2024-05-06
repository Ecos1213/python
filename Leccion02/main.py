#Operadores de operacion, nos sirve para comparar si dos valores son distintos o iguales
a = 4
b = 2

# en este caso por presedencia de operadores primero se evalua lo que esta la derecha y luego lo que esta en la izquierda osea que primero hara la igualdad y despues asignara el resultado
resultado = a == b  # a es igual a b?; este es el simbolo de igualdad en python ==
print(f'Resultado == : {resultado}')

# la presedencia en este caso sucede lo mismo que con el caso anterior
resultado = a != b  # a es diferente a b?; este es el simbodo de diferente en python !=
print(f'Resultado != : {resultado}')

# la presedencia en este caso sucede lo mismo que con el caso anterior
resultado = a > b  # a es mayor a b?; este es el simbodo de mayor en python >
print(f'Resultado > : {resultado}')

# la presedencia en este caso sucede lo mismo que con el caso anterior
resultado = a >= b  # a es mayor o igual a b?; este es el simbodo de mayor e igual en python >=
print(f'Resultado >= : {resultado}')

# la presedencia en este caso sucede lo mismo que con el caso anterior
resultado = a < b  # a es menor a b?; este es el simbodo de menor en python <
print(f'Resultado < : {resultado}')

# la presedencia en este caso sucede lo mismo que con el caso anterior
resultado = a <= b  # a es menor o igual a b?; este es el simbodo de menor e igual en python <=
print(f'Resultado <= : {resultado}')