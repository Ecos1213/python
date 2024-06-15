def miFuncion(nombre, apellido): # hay diferencia entre argumento y parametros los parametros son variables definidas en la funcion y el argumento son valores que pasan cuando llamamos a la funcion
    print('Saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}') # podemos usar los parametros dentro de nuestra funcion

miFuncion('Juan', 'Perez') # aca pasamos los argumentos que ya son los valores ( ya sea que estos valores esten en una variable o pasar los datos fijamente), si no pasamos estos argumentos nos dara un error por que son obligatorios no opcionales
miFuncion('Karla', 'Lara')



