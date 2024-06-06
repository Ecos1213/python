#sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

# ejercicio 1. iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3

# ejercicio 2. crear un rango de numeros de 2 a 6, e imprimelos

# ejercicio 3. crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

# el metodo range tiene 3 parametros desde donde comienza(opcional), donde termina (este campo es requerido), e incremento (opcional) y recuerda que esto creara un array con los numeros segun los parametros que pasemos, si colocamos el paramertro incremento tenemos que colocar el parametro de inicio para que funcione y si queremos imprimir digamos hasta el 6 en el fin tenemos que colocar como arguemnto final 7 ya que aun colocando inicio en 2 contara de 0 a 6 (7 numeros)
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11): # este range crea un array de 0 a 10 recuerda que se coloca 11 por el 0 tambien lo incluye
    if i % 3 != 0: # si el mod de 3 es diferente a 0 entonces que continue en la siguiente iteracion
        continue
    print(i) # imprimirea de 3 en 3 comenzando en 0
else:
    print("Fin del ciclo")

print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7) # este range creara 7 numeros en un array de la siguiente manera [2,3,4,5,6] como vemos son solo 5 numeros pero se debe colocar el final incluyendo el 0 y 1 de ahi abri 7 numeros
for i in rango:
    print(i) #imprimira de 2 a 6
else:
    print("Fin del ciclo")

print('Rango con valores de inicio = 3, fin = 10 y el incremento = 2')
rango = range(3, 11, 2) # este range creara un array de la siguiente manera [3,5,7,9] como vimos anterior recuerda que el argumento 11 (que es donde termina el range) quiere decir que tomara de 0 hasta 10 aun si inicia en cualquier valor que coloquemos como argumento y ademas esto incrementara de 2 en 2 los numeros que estan acutales por eso 3, 5, 7, 9
for i in rango:
    print(i) #imprimira de 3 incrementando de 2 en 2
else:
    print('Fin del ciclo')



