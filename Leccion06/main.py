# en python en los argumentos variables tambien podemos de en vez de pasar una tupla podemos pasar un argumento variable tipo diccionario
def listarTerminos(**terminos): # con dos asteriscos hace referencia de que ese argumento es un un argumento variable de tipo diccionario, en python en su manual el argumento se llama kwargs hace referencia a un argumento variable de tipo diccionario y es de buena pratica llamar a los argumetnos tipo diccionarios kwargs pero igual se puede colocar cualquier tipo de palabra
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos() # una cosa a tener en cuenta es que tanto los *args y los **args cuando llamamos el metodo podemos dejarlo vacio por que se puede pasar todos los terminos que queramos o dejarlo vacio y no sucedera ningun error asi sea que lo dejemos vacio
listarTerminos(IDE='Integrated Development Environment') # como vemos la llave no lleva comillas por eso IDE no tene comillas y el valor puede ser cualquier tipo de dato, para pasar el diccionario primero necesitamos colcoar la key despues el igual = y por ultimo el valor dentro del parentesis del llamado de la funcion, si queremos passar mas argumentos simplemente colcoamos , y dejamos la misma secuencia explicada
listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')

def listarTerminos2(nombres, *args, **terminos): # tambien podemos colocar argumentos normales con argumentos varibles tipo tupla y argumentos variables tipo diccionario y podemos usarlo pero esto lo veremos mas detalladamente mas adelante
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

