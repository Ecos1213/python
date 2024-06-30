class Persona:

    def __init__(self, nombre, apellido, edad): # estos son parametros de nuestra clase que llegaran por medio del constructor, estos parametros tienen que llamarse igual que los atributos de nuestras clases por buenas praticas
        self.nombre = nombre # como vemos hay dos variables distintas las self son nuestros atributos de nuestra clase y las que no tienen self realmente son parametros que viene del constructor y esto nos sirve para inicializar los valores por medio del constructor, estos parametros tienen que llamarse igual que los atributos de nuestras clases por buenas praticas ya que esto va a ser comun en la vida real
        self.apellido = apellido
        self.edad = edad

print(type(Persona))

#persona1 = Persona() # este es el constructor de la clase que es invisible pero realmente lo que hace el constructor invisible es llamar a init pero si corremos el codigo sin argumentos nos dara un error ya que init esta pidiendo en este caso 3 argumentos (recuerda que el self lo pasa automaticamente y es el mismo objeto que se instancia) y son obligatorios, ademas que el constructor invisible como init pide estos argumentos el constructor invisible tambien los pedira para pasarlos al init, para corregir este error simplemente pasamos los prametros que solicita el constructor un tip a tener en cuenta es que si quitamos y colocamos los parentesis encima dentro del parentesis nos mostrara que incluso pasa el self automaticamente que es la esta misma instancia y nos pide los parametros
persona1 = Persona('Juan', 'Perez', 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)