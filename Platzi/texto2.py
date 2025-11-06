# Indice 0123456789
texto = "Este es un texto"

# en python podemos tomar un caracter simplemente colocandole el indice de la
# posicion en []
print(texto[0])

# El slicing es tomar una parte del texto y se usa con posiciones dentro de
# el simbolo [] y dice que va de una posicion hasta un limite
print(texto[0:4])  # Tomara desde el indice 0 hasta 4 posiciones
# Al no incluir primero numero ira desde el principio y hasta la posicion que
# queremos
print(texto[:7])
# Tomara desde el indice 5 hasta el final (al no colocar el numero de
# posiciones a tomar python tomara hasta el final)
print(texto[5:])
# esto toma desde el indice 5 hasta la posicion -2 osea que ira hasta la x
# ya que 0 es -1 y t es -2 ya que no incluye el -2
print(texto[5:-2])

curso = "Este curso es de Javascript"
# El metodo replace replaca un texto por otro en este caso javascript por
# python y remplazara todas las palabras en este caso que sean Javascript a
# Python
print(curso.replace("Javascript", "Python"))

# El metodo split nos permite dividir en un texto segun el parametro en array
# Segun su division
textoDividido = texto.split(" ")
print(textoDividido)

# Normalizacion, en ciertos casos es importante tener en cuenta que hay que
# volver minusculas los textos

texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print("mayusculas".lower() in texto2.lower())
