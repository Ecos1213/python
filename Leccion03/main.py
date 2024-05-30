"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionara un valor entre 0 y 10
Si esta entre 9 y 10: imprimira una A
Si esta entre 8 y menor a 9: imprimira una B
Si esta entre 7 y menor a 8: imprimira una C
Si esta entre 6 y menor a 7: imprimira una D
Si esta entre 0 y menor a 6: imprimira una F
cualquier otor valor debe imprimir: valo incorrecto
por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""

calificacion = int(input('Proporciona una calificacion entre 0 y 10: '))
mensaje = None
#si esta entre 9 y 10, imprimir A
if 9 <= calificacion <= 10: # esto es lo mismo que calificacion >= 9 and calificacion <= 10 y recuerda que esto solo funciona con and
    mensaje = 'La calificacion es ' + str(calificacion) + ' y tienes una A'
elif 8 <= calificacion < 9:
    mensaje = 'La calificacion es ' + str(calificacion) + ' y tienes una B'
elif 7 <= calificacion < 8:
    mensaje = 'La calificacion es ' + str(calificacion) + ' y tienes una C'
elif 6 <= calificacion < 7:
    mensaje = 'La calificacion es ' + str(calificacion) + ' y tienes una D'
elif 0 <= calificacion < 6:
    mensaje = 'La calificacion es ' + str(calificacion) + ' y tienes una F'
else:
    mensaje = 'Valor incorrecto'

print(mensaje)
