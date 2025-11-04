# String: cadena tipo texto, hay tres tipos de formas para generar textos
# Comillas Simples
comillasSimples = 'Este es un texto'
# Comillas Dobles
comillasDobles = "Esto es un texto"
# Comillas triples
comillasTriples = '''Comillas triples'''
print(comillasSimples)
print(comillasDobles)
print(comillasTriples)

# Integers: Numeros

a = 1
b = 3.14
c = 5 + 2j  # j es un numero imaginario y esto actuaria como una ecuacion

print(a)
print(b)
print(c)

# Lista: una lista es una coleccion de datos ordenadas mutable de datos
# En el cual cada elemento tiene un indice, una posicion
lista = [0, 1, 2, 3, 4, 5]

# Tuplas: Una tupla es una coleccion de datos ordenadas inmutables de datos
# es lo mismo que una lista pero es inmutable
tupla = ("a", "b", "c")

# Diccionario: es un objeto literales, es una
# coleccion ordenada de pares de clave: valor que vamos
# a poder modificar a futuro
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Conjutos (sets): coleccion desordenadas que es mutable pero sus elementos
# son unicos
conjuto = {1, 1, 2, 2, 3}  # Output: {1, 2, 3}
print(conjuto)  # los elementos repetidos son ingnorados

# booleanos
booleanoVerdadero = True  # True y False se escribe primera mayuscula
booleanoFalso = False
