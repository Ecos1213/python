import random
x = 1  # integer
y = 2.5  # float
z = 1j  # imaginarios (complex)

print(type(x))  # con el metodo type podemos saber que tipo es la variable
print(type(y))
print(type(z))

# Tanto los numeros flotantes y enteros pueden tomar valores positivos y
# negativos
positivo = 5
negativo = -5
flotantePositivo = 5.5
flotanteNegativo = -5.5

# en los complejos osea imaginarios podemos tener tanto enteros
# como positivo y negativos
imaginario = -5 + 1j

# casteo o conversion de tipo
xflotante = float(x)  # integer a float
print(type(xflotante))
print(xflotante)

# al convertir de float a integer lo que hace es quitar despues del punto
# decimal
yEntero = int(y)  # tener mucho cuidado al castear de flotante a numero
print(type(yEntero))
print(yEntero)

# se puede castear de numero o float a complejo(imaginarios) pero no de
# complejo(imaginario) a entero o flotante
entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo)
print(type(enteroComplejo))
print(flotanteComplejo)
print(type(flotanteComplejo))

# lo que hace python al castearlo a complex es colocarle un +0j

# con import incluimos librerias de python y improtamos random para generar
# numero aleatorios del 1 al 10
# con el metodo randrange generamos numeros aleatorios de 1 a 9 (se coloca 10
# por que 10 es el limite por eso llega hasta 9)
print(random.randrange(1, 10))  # Output numero aleatorio entre 1 y 9
