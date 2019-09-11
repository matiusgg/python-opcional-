# Hacer un buscador en donde la persona ponga el pais
# y le salga las razas de ese pais

# importar librerias de python
import os

import razas_paises as paises
from documentacion.razas import razas


def razas_funcion(pais, razas):

    for llave, valor in razas.items():

        if pais == llave:

            print(f'Aqui estan las razas del pais {llave} : {valor}')

            agregar = input('Agrega una nueva raza')

            razas[llave].append(agregar)

            print(' '.join(razas[llave]))

            print(
                '**************************************************************************')
            print('************************************************************************')


print(razas_funcion(paises.pais, razas))
