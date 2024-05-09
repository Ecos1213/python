vacaciones = True
diaDescanso = False

#if not vacaciones or not diaDescanso: #asi como en php o javascript podemos denegar el true por false o el false por true en php y javascript se usa ! pero en este caso se usa el not antes de la variable, pero como estamos denegando las dos podemos encerrar con un parentesis para que cuando de el resultado deniege el resultado
if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')
