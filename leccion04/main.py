# en python no se puede hacer ciclos for de esta manera: for i = 1; i < 5; i++ ya que tiene una manera diferente de hacerlo y es usando un foreach que vaya de 0 a 5 y se hace de la siguiente manera
# for i in range(6): # como vemos el metodo range lo que hace es un array de numeros de un rango estipulado en su parametro podemos colocar solo un parametro de numero que esto significa que creara un array de 0 al numero que coloquemos como parametro en este caso seria hasta 6 pero incluso podemos hacer que sea de 1, 5 que seria que empezaria de 1 hasta 5 osea crearia un array de (1,2,3,4,5) y ya el ciclo for (foreach de python) se encargaria de recorrer cada uno y lo colocara en la letra i cada uno
#     if i % 2 == 0: # numeros pares
#         print(f'Valor: {i}')

# como vimos lo comentado anteriormente usamos un for que recorra de 0 a 6 y imprima los numeros paras esto lo podemos hacer con el shortcut continue
for i in range(6):
    if i % 2 != 0: # if para saber si es un numero impar
        continue  # lo que hace continue es no ejecutar las siguientes lineas de codigo y salta a la siguiente iteracion del ciclo
    print(f'Valor: {i}')