import math

def raiz_cuadrada(grupoNumeros):


    #* Si necesitamos hacer en la pruebas de la documentacion un for, listas, condicionales. Podemos hacerlos.
    #* Pero como hacer la identacion, es decir, el espacio que se tiene que respectar en python cuando abrimos un bucle
    #* o condicional, metodos, etc. Lo hacemos con '...' YA QUE SI NO LO PONEMOS LA DOCUMENTACION NO LO RECONOCERA.
    """
    La funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasados por parametro
    en otra lista.

    Pruebas:
    >>> listaN = []
    >>> for i in [4,9,16]:
    ...     listaN.append(i)
    >>> raiz_cuadrada(listaN)
    [2.0, 3.0, 4.0]


    """
    #* SHORTCUT FOR
    return [math.sqrt(n) for n in grupoNumeros]

# listanumeros = [25, 81, 16]
# print(raiz_cuadrada([4,9,16]))

import doctest

doctest.testmod()