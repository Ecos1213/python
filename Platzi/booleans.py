v = True
f = False


print(v)
print(f)


print(5 > 3)  # Verdadero
print(3 > 5)  # Falso

print(type(v))
# cuando es un texto contenido y convertimos a booleano, al tener texto dara true
print(bool("Hola Mundo"))
print(bool(""))  # al no tener texto dara False

# True
print(bool("abc"))
print(bool(123))
print(bool(["manzana", "pera"]))


# False
print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))

x = 123
# con el metodo isinstance podemos verificar si la variable es de un tipo de dato en especifico
print(isinstance(x, int))
