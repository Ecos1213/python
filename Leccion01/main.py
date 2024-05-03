#Cadena (string)
miGrupoFavorito = "Metallica" + " " + "The Best Rock Band"  #como en javascript se puede concatenar string con el simbolo + recuerda que como javascript en este caso la concatenacion con el + lo que hace es concatenar y no sumar, por que determina que ambos son string pero hay que tener siempre cuidado con esto
miGrupoFavorito = "Metallica"  " "  "The Best Rock Band" #si las cadenas son adyacentes, podemos omitir el operador de + y tambien se concatenan en automatico, por eso quite los + por que el " " tiene a la izquierda como a la derecha un string y pude omitr el +
comentario = "The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito)  #tambien podemos concatenar dentro de un parametro de una funcion en este caso en print
miGrupoFavorito = "Metallica"
print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)
print("Mi grupo favorito es:", miGrupoFavorito, comentario) #otra forma de imprimir varias variables es usando las , en el metodo print, esta manera automaticamente colcoara espacio en blanco por cada parametro que le pasemos

#un error comun cuando estamos comenzando en la programacion es que concatenemos dos valores esperando realizar una suma y lo que realmente obtegamos es una concatenacion por ejemplo:
numero1 = "1"
numero2 = "2"

print(numero1 + numero2)  #como vemos de en vez de realizar la suma que deberia ser 3 esta dando 12 por que realiza la conctaneacion ya que son dos strings

#si queremos sumar tenemos dos opciones podemos convertir estos dos valores en int o podemos usar una litera(una literal es lo que se conoce cualquier tipo de dato o valor) de tipo entero
numero1 = 1
numero2 = 2
#como vemos si las variables son string lo que hace es concatenar y si son int lo que hace es sumar esto se le conoce sobrecarga de operadores
print(numero1 + numero2)  #como vemos las variables la igualamos a numericas para poder realizar la suma, pero esto hace perder el anterior valor, para este problema lo que podemos hacer es convertir el tipo de dato de string a int sin perder el valor

#la segunda opcion es convertir de tipo string a entero, a esto tambien se le llama casteo
print("Suma: ", int(numero1) + int(numero2))  #como vemos simplemente es colocar un metodo del tipo de dato al que queremos hacer la conversion, este nombre va de forma corta y como parametro pasamos la variable a convertir

#hay un problema con las conversiones numericas a cadenas es que si la cadena no es solo un numero este nos dara un error ejemplo:
#numero1 = "uno"  #para poder hacer la conversion tenemos que colocar valores validos en este caso tendria que ser numerico
#numero2 = "2"
#print("Suma: ", int(numero1) + int(numero2))

#numero1 = 1
#numero2 = "2"
#print("Suma: ", numero1 + numero2) #el error sucede tambien sucede lo mismo si uno de los valores es string e intentamos hacer la suma con un entero