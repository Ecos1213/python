# condicion = True
#
# while condicion: # asi se escribe un while en python, ejecutara el ciclo hasta que la condicion sea false
#     print('Ejecutando ciclo while')
# else: #en while tambien podemos colocar un else en python, este se ejecutara cuando la condicion del while no se cumpla y tambien es opcional colocar el else
#     print('fin del ciclo while')

contador = 0
while contador < 3:
     print(contador)
     # en python no se puede hacer los operadores de incremento que son ++ o -- por ende tiene que usarse +=
     contador += 1 # contador = contador + 1
else:
    # en el else se puede imprimir cualquier otro codigo, si el while no cumple la condicion se ejecutara este else
    print('Fin ciclo while')