# -*- coding: utf-8 -*-
# importar un paquete o modulo. En donde pytohn nos mostrara la ruta y nosotros iremos escogiendo q ue paquete y que modulo
# usaremos al final. Esto se considera un NAMESPACE, por asi decirlo, en donde podemos importar los paquetes para suarlos.

# A su vez podemos asignar un nombre a los NAMESPACE con AS
# import modulo01 as m1
# import paquete01.modulo01 as Pm1

# A su vez tambien podemos importar obviamente funciones o variables.
# Tambien podemos importar de esta manera con FROM, cuando usamos el FROM recodermos que es para importar algo especifico de un modelo, ademas 
# podemos importat mas de una funcion/variable especifica con "," para seprararlos.

# from paquete01.modulo01 import funcion01 as Fm1
# from paquete01.modulo02 import funcion01 as Fm2

# Un problema que s puede presentar es que si importamos algo de archivos diferentes pero las funciones ovariables, etc.
# tienen el mismo nombr, no habria problema porque con AS podemos nombraRLAS COMO QUERAMOS Y DIFERENCIARLAS

'''
JERARQUIA DE IMPORTACION DE MODULOS:

1. IMPORTAR PRIMERO, LOS MODULOS DEL PROPIO PYTHON
2. MODULOS DE TERCEROS
3. MODULOS DE NUESTRA APLICACION

IMPORTANTE: ENTRE IMPROTACION E IMPORTACION, DEJAR UNA LINEA DE CODIGO EN BLANCO, Y CUANDO TERMINOS LAS IMPORTACIONES
DEJAR DOS LINEAS EN BLANCO.

Ademas el __init__.py nos permitra interactuar entre modulos para poder importarlos sin necesidad de salir entre carpetas ya que este le indica que 
nuestro archivo es un paquete, es decir,
python ya sabe donde estan porque lo reconoce como paquetes, por lo cual si hacemos PAQUETEs es porque vamos a incluir todo
lo que encesitamos dentro de esta sin necesidad de poner un archivo que necesitamos fuera de ese paquete, ya que le constaria mas a python
saber donde esta.

PEP 8: En evernote esta las reglas que debe seguir python o consejos para tener un codigo limpio,
El pep8 lo usa la comunidad para asegurar la sintaxis del python correctamente. por lo cual para ponerlo da:
F1->linter python->pep8. Lo instalamos y ylisto.
En nuestro caso nos beneficia para los import y su jerarquia

Ademas instala el pluggin PRETTIER para que nos corriga el codigo y nos lo organice, pero como lo hacemos?
pon click en el archivo que quieres organizar y pon SHIFt + ALT + F y nos lo hara. Si no nos lo hace nos preguntara si hemos instalado
el PEP 8 formateador, lo instalamos y volvemos a hacerlo. Ten en cuenta que antes debes haber cambiado el LINTER por el PEP8.
'''
'''
Los paquetes son las carpetas qe albergan los modulos(archivos de python).
Dentro de un paquete tenemos que generar un __INIt__.py vacio, Este nos permitira,
y los paquetes pueden tener Subpaquetes, y estos tendrian sus modulos con __INIT__.py tambien
__ INIT__: Es para inicializar el paquete.


'''

'''
GENERADORES EN PYTHON:
Son estructuas que extraen valores de una funcion, es decir que ya estan dentro de las funciones
y se alamacenan en objetos iterantes(Son objetos que se pueden iterar, es decir por ejm si ahcemos un bucle podemos iterarlos para
scarles la informaicon9), se almacenan en 1 en 1, y cuando se almacenan ese valor, se le llama "SUSPENCION DE ESTADO".

FUNCIONES: Cuando hacemos una funcion, la declaramos, tenemos un return si es el caso, la llamariamos
GENErADOREs: Tambien se declara de la misma forma que una funcion, lo mismo tendria return si fuera el caso, tambien la llamarias

POR LO CUAL, que es lo9 que ocurre cuando. Cuando usamos el sistema de funcione stradicionales, estamos ahciendo esa peticion en donde
1) llamamos la funcion, 2) infresa en el ocidgo de lafuncion para analizar, 3) ejecuta la funcion, 4) vuelve a la linea del llamado
En si esto, ocupa mucha memoria es el codigo ejecutable es muy largo, por lo cual recurririamos en un gENERADOR.
Lo cual es hacer una funcion misma, pero la diferencia es que al momento de llmar la funcion, sucede que se genera una estructura
la cual esta en pausa, es decir, en vez de almacenar toda la informacion, esta de vuelta solo almacena un pedazo de informacion
por lo cual no acumula una excesiva cantidad de memoria, Esto nos viene bien para gestionar para encerrar el uso de memoria a la minima expresion
En si, nos brindara la informacion por pedazos en donde si vamos haciendo print's por ejemplo nos ira mostrando cada vez mas, mas pedazos

'''

'''
EJM GENERADOR: FUNCION DE NUMEROS PARES
'''

# Funcion Tradicional. Te ejecuta todo y alamcena mas memoria

# def numPares():

#     pares = []
    
#     while True:
    
#         numero = int(input('Ingresa el numero par que quieras ingresar'))

#         if numero % 2 == 0:

#             pares.append(numero)

#             for i in pares:

#                 print(f'numeros: {i}')
        
#         else:

#             print('No es un numero primo')

        
#     print(pares)


# numPares()



# GENERADOR. Te ejecuta solo una parte, con la itencion de no alamcenar todo en memoria
# y solo un pedazo. Esto para monitoriar o gestionar la informacion recibida de la funcion

# EL profe lo hizo de otra forma como yo, pero la idra aqui es captar elconcepto
def numPares_Generador(cantidad):

    num = 1

    # No es necesario una lista para introducir los pares

    while num < cantidad:
        # YIELD: Contruye un objeto iterable, almacenando los elementos en uno en uno
        # No necesitamos un RETURN, en este caso para devolver los pares

        yield num * 2

        num += 1

# Colcoamos la llamda en una variable que nos permita al momento de hacer un bucle
# poder ir mostrando la itineracion del objeto del generador

resultado = numPares_Generador(5)

# Hacemos el FOr para comprobar la itineracion

for i in resultado:

    print(i)

# Pero si queremos solo que nos muestre un dato y no toda la itineraciond el objeto
# usamos NEXt: Nos permite observar una parte de la itineracion y cada vez que pongamos un nuevo
# NEXt nos mostrara el siguiente dato/elementos/parte de la itineracion

print(next(resultado))
print(next(resultado))

print(next(resultado))

print(next(resultado))




       