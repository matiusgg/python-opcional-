"""
BUSCAR PRATRONES
----------------
EMPLEAREMOS:
MATCH: Si hay coincidencias al inicio de un string.
SEARCH = Busca en todo el STRING

"""

import re

persona1 = 'Pedro Antonio'
persona2 = 'Antonio Morrón'
persona3 = 'María Lucia'
persona4 = 'Pati Fort'

#* MATCH ***********************
if re.match('Pati', persona4):

    print('Encontrado')
else:
    print('No encontrado')

#* MATCH admite un tercer parametro
#* Vamos a hacer que MATCH ignore las mayusculas y minusculas
#*METARACTER(.): Nos sirve para saber si encuentra palabra que termine depsues del punto.
#* IGNORECASe: Nos permite ignorar las amyusculas y minusculas en la busqueda.
if re.match('.ati', persona4, re.IGNORECASE):
    print('Encontrado')
else:
    print('No encontrado')

#* SEARCH ************************************
if re.search('Antonio', persona2, re.IGNORECASE):
    print('Encontrado')
else:
    print('No encontrado')

codigo = 'fdefrgtghghjfgjfhj7hghm'
#* Si a lo largo de una cadena de texto  existe un patron concreto.
if re.search('7', codigo, re.IGNORECASE):
    print('Encontrado')
else:
    print('No encontrado')