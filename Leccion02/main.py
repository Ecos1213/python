"""
Instrucciones de la tarea:

- En el siguiente ejercicio se solicita calcular el area y el perimetro de un rectangulo,
para ello deberemos crear las siguientes variables

alto(int)
ancho(int)

- El usuario debe proporcionar los valores de largo y ancho, y despues se debe imprimir el resultado en el siguiente formato
(no usar acentos y respetar los espacios, mayusculas, minusculas y saltos de linea):

Proporciona el alto:
proporciona el ancho:
Area: <area>
Perimetro: <perimetro>

Las formulas para calcular el area y el perimetro de un rectangulo son:
Area: alto * ancho
Perimetro: (alto + ancho) * 2

"""
# en python podemos tambien realizar comentarios con tres veces comillas dobles y este comentario es comentario multilinea


alto = int(input("Proporciona el alto del rectangulo: ")) #tener cuidado con los acentos en python por que puede que no abra el archivo o aparezca una respuesta erronea
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2  #recuerda que la presedencia de operadores es importante en la programacion por eso el perimtro lleva parentesis para que primero haga la suma y despues la multiplicacion, recuerda que la multiplicacion tiene mas presedencia de operadores que la suma por lo tanto si no colocamos el parentesis primero ejecutara la multiplicacion
print(f'area: {area}')
print(f'Perimetro: {perimetro}')
