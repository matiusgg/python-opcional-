import os

import razas_paises as paises
from documentacion.razas import razas



def Generador(pais, razas):


    for llave, valor in razas.items():

        if pais == llave:

            agregar = input('Agrega una nueva raza')

            razas[llave].append(agregar)

            for valores in valor:

                yield valores


print('************************************************'
''
'********************************************************')
razasGenerador = Generador(paises.pais, razas)

for i in razasGenerador:

    print(i)


    print('********************')


# print(next(razasGenerador))




