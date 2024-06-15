def sumar(a, b):
    # recuerda return devuelve el valor de la funcion y al usar la palabra return las siguiente lineas de codigo no se ejecutaran
    # total = a + b
    # return total
    return a + b # podemos retornar dos maneras diferentes una variable o colocar la operacion aritmetica que igual devolvera el resutado no mas de la operacion, en esta expresion los parentesis son opcionales pero es bueno colocar parentesis a otras expresiones

resultado = sumar(5, 3) # como en la funcion estamos retornando un valor, este valor podemos asignarlo a una variable, recuerda lo que hara el codigo es entrar a la funcion ejecutara la linea de codigo y al tener un return ejecutara el codigo hasta return y devolvera el valor y despues se hara la asignacion a la variable este podemos verlo con el debug mode (para entrar a la funcion en debug mode tenemos que usar step into o la flecha hacia abajo cuando llege a la funcion)
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar(5,3)}') # tambien lo que podemos hacer es simplemente llamara la funcion y al retornar el valor solo imprimira su valor