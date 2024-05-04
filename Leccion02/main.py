operandoA = 3
operandoB = 2
suma = operandoA + operandoB  # usamos el operador de addicion en este caso hara una sumatoria y no una concatenacion esto es por que ambos son numericos y no strings
print('Resultado de la suma:', suma)  #si queremos usar menos carateres podemos usar mejor comillas simple para definir strings
print(f'resultado suma: {suma}')  # hay otra manera de inprimir en python que es el f literal, colocamos dentro como parametro en el print la letrra f y despues colocamos un string en comillas simples o dobles dentro del string podemos usar la interpolacion que son llaves dentro del string {} y la variable a imprimir dentro de estas llaves y esto nos imprimira el resultado, esto es como javascript cuando usamos ´´

resta = operandoA - operandoB #operando de resta
print(f'Resultado de la resta: {resta}')

multiplicacion = operandoA * operandoB  #operando de multiplicacion
print(f'Resultado de la multiplicacion {multiplicacion}')

division = operandoA / operandoB  #operando de la division, podemos ver que en el resultado da 1.5 esto quiere decir que python automaticamente transforma la variable division en punto flotante
print(f'Resultado de la division: {division}')

division = operandoA // operandoB #operando de la division que solo nos devuelve tipo entero, como vemos en el anterior ejercicio de la diviosion python automaticamente nos convirtio la division en punto flotante si no queremos que haga esto podemos usar // para que solo nos entre de la division el entero y no mas
print(f'Resultado de la division entera(int): {division}')

modulo = operandoA % operandoB  #operando de modulo o residuo
print(f'Resultado residuo division (modulo): {modulo}')

exponente = operandoA ** operandoB #operadxor de exponente, esto es 3 elevado a la 2 osea 3 * 3 y da 9 recuerda que la base es el operadorA y el exponente el operadorB
print(f'Resultado del exponente {exponente}')