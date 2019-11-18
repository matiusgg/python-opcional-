"""
EXPRESIONES REGUALRES: Encontrar algo especifico en un texto.
"""

#* Inicializamos la libreria de expresiones regulares(REGX)
import re

frase = 'hoy es lunes y me suenan las tripas de no poder comer paella'

# SEARCH, nos ayudara a buscar algo especifico en el texto. nos dira mediante un objeto: MATCH: Es que existe, 
#* y SPAN nos dira en que caracter comienza y termina dentro del texto.
print(re.search('paella',frase))

palabra = 'paella'

#* Si la busquedaq donde si la palabra esta en frase. SEARCH si no encuentra nada nos devuelve un NONE.
if re.search(palabra, frase) is not None:
    print('Texto encontrado')
else:
    print('Texto No encontrado')

#* Alamcenamos el objeto en una variable
buscar = re.search(palabra, frase)

#* Primera posicion donde se encuentra el SPAN. Cuando SEARCH crea el objeto, nos genera el SPAN, y mediante
#* START: Podemos ver en que posicion dentro del texto inicia palabra.
print(buscar.start())
#* En cambio si queremos ver cuando termina dentro del texto.
print(buscar.end())
#* Si queremos reunir la primera  y ultima posicion, lo ponemos en una TUPLA.
print(buscar.span())

