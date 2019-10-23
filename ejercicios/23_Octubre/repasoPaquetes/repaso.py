'''
Para python ya un archivo .py ya es un modulo

Si necesitamos modulo que sean ejecutables en cualquier situacion, es decir dentro del proyecto.
Donde no importe le lugar donde tengamos el archivo, podamos importarlo y a su vez que en el main.py reconozca
el paquete.
Para ello usamos el paquete, que pytohn lo interpretara como una libreria por asi decirlo,
pero para que una carpeta se convierta en un paquete usamos el modulo __init__.py
Y dentro de esta carpeta ponemos los modulos de nosotros que vamos a importar al main.py
Es importante que si vamos a tener mas de un modulo en el paquete, se relacionen mediante los nombres es decir mendiante
un sujito tanto para el nombre del paquete como para los modulos dentro del paquete.
Ejm:
NombrePaquete: calculos
__init__.py
modulo: calculos_basicos.py , calculos_avanzados.py

Como vemos estos modulos tiene el sufijo del nombre del paquete, esto nos ayudara para identificar mas facilmente
que estos modulos vienen de ese paquete.

Ya en el main,py o donde vamos a importar el paquete, es importante que al momento de importarlo
la extension de python sepa identificar el paquete dentro de las librerias, por lo cual si identifica
el paquete identificará los modulos de ese paquete, y si usamos from, evidentemente podremos usar
importar algo especifico de ese modulo

ejm: from calcular.calculos_basicos import *

SETUP:PY
NOs permitira decirle a python que es lo queremos ahcer con un paquete, lo que hacemos es

'''