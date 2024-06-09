# Dada la siguiente tupla
# crear una lista ue solo incluya los numeros menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

# Definir la lista
lista = []

# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento > 5:
        continue
    lista.append(elemento)

# imprimimos la lista
print(lista)

del lista
del tupla

