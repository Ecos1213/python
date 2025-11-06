# Podemos usar comillas simple y dentro comillas dobles
# O podemos usar comillas dobles y dentro comillas simples
print("Hola 'Mundo'")
print('Hola "Mundo"')

ingles = "I'm Sergie"

# Esto nos permite escribir en multiples lineas
multiples = """Hola
Mundo
desde
las
comillas
triples
"""

print(ingles)
print(multiples)

palabra = "Murcielago"
print(len(palabra))  # El metodo len dice cuantos caracteres tiene el string

texto = "Este curso es de fundamentos de Python"
# De esta manera podemos saber si el string de la izquierda esta incluida en
# el string de la derecha, para eso sirve el keyword in y de vuelve un booleano
estaIncluida = "Python" in texto
# Da True por que es case sensitive (sensitivo a mayusculas y minusculas)
print(estaIncluida)  # True

estaIncluida = "python" in texto
print(estaIncluida)  # False

# En python not in sirve para decirle si no esta incluido en el texto
# Recuerda que es case sensitive (sensitivo a mayusculas y minusculas)
noEstaIncluida = "Javascript" not in texto
print(noEstaIncluida)  # True

mayuscula = texto.upper()  # El metodo upper vuelve el texto en mayuscula
minuscula = texto.lower()  # El metodo lower vuelve el texto en minuscula

print(mayuscula)
print(minuscula)


espacios = "             Este es el texto            "
sinEspacios = espacios.strip()  # Strip quita espacios al principio y al final

print(sinEspacios)
