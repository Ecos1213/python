edad = int(input('Introduce tu edad: '))
#edad >= 20 and edad < 30 # esto es lo mismo que el primer conjunto de operador logico de and
#edad >= 30 and edad < 40 # esto es lo mismo que el segundo conjunto de operador logico de and
if (20 <= edad < 30) or (30 <= edad < 40):  # en python podemos simplicifar mas la condicional del if, que es simplificando y cambiando los operadores logicos, simplemente quitamos las dos variables de edad y la dejamos en el centro y dejamos el operador logico de la derecha igual el que tiene que cambiar e invertirese es de la izquierda ya que como vemos la primera expresion es >= pero como ahora pasa al lado derecho del numero entonces hau que invertir el > por < ya que estamos preguntando si edad es mayor que el numero
    #esto se lee igual osea edad es mayor o igual que 20 y edad es menor a 30 o 30 es menor o igual que edad y es menor que 40
    print('Dentro de rango (20\') o (30\'s)')
else:
    print("No esta dentro de los 20's ni 30's")

