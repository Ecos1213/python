#condicion = True #con booleano nos funcionara la condicion y pasara por verdadero en este caso
#condicion = 10 # pero si usamos un numero nos dara tambien la condicion veradera ya que tiene algo y lo toma como verdadero si no tuviera nada esto nos daria la condicion false
condicion = '' # esto tambien sucede si es una cadena de texto vacia nos darala la condicion falsa si esta llena nos dara la verdadera, hay que tener mucho cuiado con esto

if condicion:
    print('Condicion verdadera') #python nos agrega una tabulacion despues de los puntos, python no usa llaves para abrir o cerrar bloques de codigo, con python solo los espacios en blanco en este caso la identacion es suficiente para que lo interperte como un nuevo bloque de codigo y todas las lienas que tengan un tabulador
    # si no agregamos un tabulador o un solo espacio en el print nos dara un error por no indentar
else:
    print('Condicion falsa')


#en esta siguiente linea de codigo ya estamos una condicion mas detallada diciendo que si es un booleano true o un booleano false imprima algo si no imprima condicion reconocida

if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion no reconocida')