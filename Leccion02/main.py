#Operadores logicos en python
"""
los operadores logicos son:
operador               descripcion                                            uso
and                    devuelve True si ambos operadores son true             a and b
or                     devuelve True si alguno de los operadores es True      a or b
not                    devuelve True si alguno de los operandos False         not a
                       esto quiere decir que si el valor es True
                       cambia a False o si es False cambia a True

en el uso puede ser una expresion o un valor booleano
y el operador not es unario osea que necesita de un operador para funcionar o el resultado de una expresion o el valor de a

"""

a = True
b = False
resultado = a and b  # esto es false
print(resultado)

resultado = a or b  # esto es true
print(resultado)

resultado = not a  # esto es false
print(resultado)

# el operador and y or son operadores binarios ya que se necesitan de dos valores para poder ejecutarse
# el operador not es unario ya que se necesita solo de un valor para poder ejecutarse