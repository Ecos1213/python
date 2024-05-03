#Tipos bool (boolean)
miVariable = True  #recierda que se debe escribir en forma capitalizen que es que la primera letra tiene que ir en mayuscula si no python no lo reconocera
print(miVariable)

miVariable = False
print(miVariable)

miVariable = 3 > 2
print(miVariable)

miVariable = 1 > 2
print(miVariable)

#como vemos nos adelantamos un poco usamos el if en python y como vemos la variable no lleva parentesis y no lleva llaves {} si no : y automaticamente nos identa el codigo por que lo que pasa es que python identifica lo que esta dentro es gracias a la identacion del codigo e igual el else tambien funciona igual lleva : para decirle que ahi comienza el else y lo que esta identado del else para abajo es parte del else hasta las siguientes linea no sean identada
if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")