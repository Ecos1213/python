#le damos click al numero de linea de codigo para coloca run breakpoint y le damos click derecho debug mode, al lado de consola le podemos dar a las flechas el mas importante es el step over que no saltara linea en linea
condicion = True #al darle step over podemos ver que en la consola de debug que es Threads & Variables que ya aparece que la variable condicion esta en true, podemos darle step over para ver el flujo que maneja el debug

if condicion:
    print('Condicion verdadera') #python nos agrega una tabulacion despues de los puntos, python no usa llaves para abrir o cerrar bloques de codigo, con python solo los espacios en blanco en este caso la identacion es suficiente para que lo interperte como un nuevo bloque de codigo y todas las lienas que tengan un tabulador
    # si no agregamos un tabulador o un solo espacio en el print nos dara un error por no indentar
else:
    print('Condicion falsa')


if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion no reconocida')