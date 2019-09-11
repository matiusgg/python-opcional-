"""

EDAD

"""

import os


def edades(edad):

    if edad < 0:

        # RAISE: Nos permite crear un "ERROR" como una simulacion de error, es decir, podemos customizar/manejar el error
        # el python detecta, y podemos poner /cambiar lo que python nos coloca cuando hay el error, en cambio con EXCEPT en TRY:
        # nos permite manejar el error dentro de la aplicacion es decir, que si aparece el error no detengas la aplicacion.

        raise TypeError('No se permiten edades negativas CRACK')

    if edad < 20:
        return 'eres muy joven'

    elif edad < 40:

        return 'Eres joven'

    elif edad < 70:

        return 'Haz llegado a tu madurez'

    elif edad < 120:

        return 'Cuidate que estas jodido'


if __name__ == "__main__":

    os.system('clr')

    print(edades(-4))
