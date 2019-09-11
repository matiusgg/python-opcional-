"""

    COMPREHENSIONS
    --------------
    Son constructos que nos permiten geenrar una secuencia a partir de otra secuencia.

"""

cadena = input('escribe algo: ')

# Cmo vemos usamos el SHORT de for en la estructura de una lista, para que nos separe el string,
# Tambien podemos usarcondicionales y hasta funciones de una lista
# Lo importante es que entiendas que la estructura del comprehensions es asi, end donde como vemos a partir de una sentencia
# input y lista, ejecutamos otra sentencia, el cual seria el bucle

comprehensions = [i for i in cadena if i != 'z']


