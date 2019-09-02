'''
Orientacion programada a objetos en PYTHON.

El concepto es el mismo, pero la sintaxis cambia obviamente por ser otro lenguaje:

PAQUETES: Los paquetes en PYTHON se tratan de una division de archivos que cumpliran su parte dentro del proyecto
en donde un paquete basico debe tener, el MAIN(donde ira el if__main__, y lo que le pongamos para iniciar), la clase, y variables o funciones
que queramos unir a la clase.

Por lo cual para importar un archivo a otro, usamos el FROM
FROM: Nos permite importar un codigo especifico de un archivo en vez de todo.
Estructura:
from Archivo.py import nombreVariable/funcion/constante/etc.

PORQUE USAR FROM -> IMPORT: Porque esta nos permite importar algo especifico que nosotros escogamos de un archivo
 sin tener que importar todo el codigo de un archivo. Al usar este medio, si queremos usar esa variable por ejemplo
 no tendremos que especificar de que archivo viene, por ejemplo: nombrearchivo.nobreVariable ya no tendremos que usar esta manera
 sino que lo que importamos con FROM se une al archivo que recibio la importacion

Crear una clase:
class nombre(): []

    ATRIBUTOS: La cuestion con los atributos es que tenemos que definirlos con "=" si o si, si no queremos defnirlos, usamos 0 si es entero,
    si es string, pues cualquier cosa, o con boolean tambien podemos. Ademas de que no usamos el encapsulamiento como en PHP sobre PUBLIC, PRIVATE o PROTECTED.

    ejm: ruedas = 0
    ejm: licencia = true
    ejm: 

THIS en PYTHON en las clases: Cuando vamos a usar los atributos de la clase en algun metodo el THIS en python es SELF.
La cuestion aqui es que para que funcione tenemos que poner en los parametros el SELF para que funcione
y a su vez para usar los atributos ponemos antes de estos self.NombreAtributo

CONSTRUCTOR: en el constructor podemos declarar atributos, la cuestion obviamente es que los atributos que declaremos en el
constructor es porque los usaremos o los pondremos si o si.

def __init__(self, parametro, parametro, etc.):

self.ruedas = parametro

METODOS: En los metodos es como una funcion pero si queremos usar atributos entonces usamos el SELf obviamente.

ENCAPSULAMIENTO: En el encapsulamiento ya no se usan PUBLIC, PRIVATE o PROTECTED. En donde:
El PRIVATE: para indicar que un metodo o atributo es privado es usamos antes de este "__". EJM:

__Metodo():


'''
# Color negro en la consola
# \x1b[1;30m {se coloca la funcion/o lo que queramos que se encienda. Ejm: self._LAMPARA[pulsar]}]
# Donde x1b[texto:cogido de color va del 30 al 39]

# print(f'\x1b[1;32m {self._LAMPARA[1]}')

# EJERCICIO BOMBILLA: Hacer una bombilla la cual se pueda encender y apagar, y que segun determinadas veces se dañe porque la encendistes muchas veces
# 

import os
import random

class Lampara():

    _LAMPARA = [ '''
       .----------.
       |   ON   |
       |   ____   |
       |  |.--.|  |
       |  ||  ||  |
       |  ||__||  |
       |  ||\ \|  |
       |  |\ \_\  |
       |  |_\[0]  |
       |          |
       |  OFF   |
       ‘----------’
        '''
        ,
        '''
       .----------.
       |   ON   |
       |   __     |
       |  | /[0]  |
       |  |/ / /  |
       |  ||/_/|  |
       |  ||  ||  |
       |  ||  ||  |
       |  |.__.|  |
       |          |
       |  OFF   |
       ‘----------’

       '''

    ]


