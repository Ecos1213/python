# una variable es una cajita donde se guarda un valor
# para luego poder utilizarlo, esta cajita
# es un lugar en memoria donde python
# se encargara de consultarlo para poder recuperar
# ese valor que habiamos puesto
# Esto es una variable con un valor, esta variable x
# va a apuntar a un lugar en memoria y va quedar guardada esta informacion
x = "Esta es una variable"  # el igual es un operador de asignacion
# los operadores de asignacion en este caso toma el valor de la derecha lo
# asigna al operador de la izquierda
print(x)

# Ojo que python permite sobrescribir variables
# Depende donde este el codigo va a sobreescribir tener cuidado
# Si esta muy abajo sobreescribira la variable al asignar
x = "Aca estoy escribiendo otra cosa"
print(x)

# En python las variables minusculas y mayusculas son distintas
# por lo tanto si escribo una variable en mayuscula este asignara en
# otra parte en memoria
X = "Esta es otra variable"
print(x)
print(X)
# A esto se le llama keysesitive
# esto significa que es sensitivo a si es mayuscula o minuscula

# Nombres validos e invalidos para nuestras variables
mivariable = "Esta es una variable"

# podemos usar guines bajos para una variable
mi_varaible = "Esta es una variable con guion bajo"

# podemos usar guion bajo para comenzar una variable
_mi_variable = "Esta variable comienza con un guion bajo"

# podemos usar minusculas y mayusculas
miVariable = "Otra variable"

# podemos colocarla en mayusculas solamente
MIVARIABLE = "Todo mayus"

# podemos colocar numeros
miVariable2 = "Otra variable mas"

# Reglas incorrectas para crear variables
# 2variables = "No se puede utilizar esta forma"
# mi-variable = "No se puede utilizar guion medio"
# mi variable = "No se puede utilizar espacios"

# Convenciones para escribir variables:
# camelCase
camelCase = "Comienza con minusculas y el resto de las palabras con mayus"
PascalCase = "Comienza con mayuscula y el resto de las palabras tambien"
snake_case = "Se separan las palabras con guines bajos"

# Hay algunas variables que se usan para ciertas nomclaturas ejemplo:
# Variables solo en mayusculas se usan para constantes
# Variables que se inicia con guion bajo son variables privadas
