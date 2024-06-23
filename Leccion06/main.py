def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']

desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((10, 11))
desplegarNombres((10,)) # si queremos pasar o crear una tupla de un solo dato tenemos que colocar entre parentesis el dato y al final del dato una coma
desplegarNombres([10, 11])
desplegarNombres(10)
desplegarNombres(10, 11)
# python es bastante flexible pero aun asi tenemos que tener cuidado con que informacion estamos proporcionando por que si vemos estamos usando un for(foreach) que recorre un array o tupla o diciconario por ende no podemos pasar solo un numero o booleano por que dara error y tampoco podemos pasar varios parametros por que no es un argumento variable y si solo pasamos un string recorrera cada letra e imprimira cada letra por eso hay que tener cuidado e incluso tener cuidado de como vamos a tratar el dato dentro de la funcion
