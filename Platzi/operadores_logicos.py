# Operadores de Comparacion

x = 5
y = 3
z = 5


print(x == y)  # si es igual? False
print(x != y)  # si es distinto True
print(x > y)  # Es mayor a segunda, True
print(x < y)  # Es menor a segunda, False
print(x >= y)  # Es mayor o igual, True
print(x >= z)  # Es mayor o igual, True, por que son iguales
print(x <= z)  # Es menor o igual, True, por que son iguales


# Operadores logicos
# TRUE and FALSE
print(x > y and y > z)  # ambas tienen que ser true para dar true, False
# TRUE and FALSE
# una de las condiciones tiene que dar True para ser True, True
print(x > y or y > z)
# FALSE and FALSE
print(x == y or y > z)  # FALSE

v = True
f = False
print(not (v))  # negacion de booleano, cambia de true a false
print(not (f))  # cambia de false a true
