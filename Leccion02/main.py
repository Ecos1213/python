"""
  instrucciones de tarea:
  solicitar al usuario dos valores y determinar cual numero es el mayor
  solicitar al usuario dos valores:
  numero1 (int)
  numero2 (int)
  se debe imprimir el mayor de los dos numeros (la salida debe ser identica a la que sigue):
  Proporciona el numero1:
  Proprociona el numero2:
  El numero mayor es: <numeroMayor>
"""

numero1 = int(input("Proporciona el Numero 1: "))
numero2 = int(input("Proporciona el Numero 2: "))

if numero1 > numero2:
    print(f'El numero {numero1} es mayor')
else:
    print(f'El numero {numero2} es mayor')
