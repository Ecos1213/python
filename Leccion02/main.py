edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad < 40
#print(treintas)
#no es comun que nuestro codigo este separado de los operadores logicos con las condicionales por eso se comento y se colocara en las condicionales, pero esto hace perder la parte del if anidado que es el if de veintes y el elif treintas y el else que es el que le sigue

#if veintes or treintas:
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print('Dentro de rango (20\') o (30\'s)') # como vemos necesitamos colocar comilla simple dentro de la cadena, hay dos formar para que nos imprima dentro de la cadena una es usando \ (a esto se le llama caracter de escape ya que le dice al leguanje que no debe cerrar la cadena osea que no considere este caracter como el cierre de nuestra cadena) antes de la comilla simple que queremos imprimir o la otra es usando comilla dobles para iniciar la cadena y terminar la cadena con comillas dobles
#    if veintes:  # como estas condicionales esta dentro del if por su identacion, hace que este dentro del if, este if interno se le conoce un if anidado, un if dentro de un if
#        print('Dentro de los 20\'s')
#    elif treintas:  #como vemos en python no se escribe else if si no elif y hace lo mismo que un else if ya que es lo mismo
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de rango')
else:
    print("No esta dentro de los 20's ni 30's") # como vemos usamos la segunda opcion que es usar comilla doble para la cadena y poder imprimir las comillas simples

