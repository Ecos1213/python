for letra in 'Holanda': # en el ciclo for del foreach podemos colocar toda la cadena en el foreach como se ve aqui
    if letra == 'a': # usamos el if para verificar si existe una letra a y si es asi imprimeme una letra y despues con el break interrumpimos el ciclo permanentemente y por esto el else no se ejecuta
        print(f'Letra encontrada: {letra}')
        break # el break rompe el ciclo por lo tanto apenas encuentre una 'a' rompera el ciclo y no continuara y el else tampoco se ejecutara por que al romper el ciclo el else del ciclo no se ejecuta
else:
    print('Fin ciclo for')
