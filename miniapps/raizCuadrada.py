"""

RAIZ CUADRADA

"""

import math
import os

def calcular(num1):

    if num1 < 0:

        raise ValueError('El numero no puede ser negativo')

    else:

        return math.sqrt(num1)


usuario = int(input('Introduce tu numero:'))

# DIFERENCIA NAME_ERROR: Es una clase que nos permite modificar el error a nuestro antojo
# En cambio en el VALUE ERROR: ya es un error asignado por la consola, en donde ESTa el rorr pero podemos
# cambiar el nombre

try:

    print(calcular(usuario))

except ValueError as errorcito:

    print(errorcito)

print('Programa terminado')








