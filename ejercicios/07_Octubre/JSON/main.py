'''
JSON: Es un estandar basada en texto plano, se utiliza para un intercambio de informacion pertinente
Es como una base de datos minimalista, y funcional, ademas de no relacional. MONGODB se basa en JSOn
Nace de la necesidadf de encontrar un sustituto de XML. Un lenguaje
que no sea XML.

JSON vs XML
XML es el primer lenguaje estandar de intercambio.
XML pesa mucho, porque s tiene que programamr mas.
JSON ejecuta uno linea de codigo, XML ejecuta 5 lineas de codigo.
JSON lleva 100 lineas de codigo, XML lleva 400 lineas de codigo.

Compatibilidad con JSON: Obejtive C, Python, Java.
La estructura JSON:
los valores pueden ser: listas, diccionarios, strings, enteros.
{"llave": "valor"}

PARSEO en JSON buscar.
En la siguiente pagina, y escribimos un JSON, para pasarlo a PARSE.
ver en pagina json.parser.online.jr

****************************************************************************************************
PARA TRAER LA INFORMACIONQ UE TENEMOS EN JSON A PYTHON, IMPORTAMOS EL ARCHIVO DE JSON
El archivo JSON puede tener demasiada informacion por lo cual, para traer una linea con datos
ponemos with open('datos.json) as mis_datos:

        Para cargar todoas las lineas de json ponemos dentro del WITH=

        datos = json.loads(mis_datos.read())

        Ya si queremos llamar o imprimir algun dato ponemos el nombre de la variable "datos"
        y entre [] ponemos el nombre de llave del diccionario de JSON para que nos saque
        el valor. Y si una llave tiene una lista u otro diccionario dentro de el.
        Simplemente con volver a abrir los [] para acceder a ello. Al final si lo miras
        es como la estrucutra de arrays, como un arrays dentro de otro arrays como en PHP

        Podemos usar GET para llamar tambien a la llave del diccionario
'''

import json
# import os

# os.system('clr')


# with open('datos.json') as mis_datos:

#     datos = json.loads(mis_datos.read())

# print(datos)

'''
IMPORTANTE JSON: Es importante saber que cuando quieres llamar o imprimir un dato de json, ya sea que tengas un diccionario o una lista
la llave en JSON no la poder imprimir, SOLO LOS VALORES, por lo cual si quieres imprimir una llave tendras que ponerla como valor
Una forma mas comoda seria, con la siguiente estructura:

[

    {
        "animal": "mono",
        "descripcion": "Me has llamado mono? si quieres te doy una ensalada de puñetazos. CRACK"
    },
    {
        "animal": "gallo",
        "descripcion": "Me has llamado mono? si quieres te doy una ensalada de puñetazos. CRACK"
    }

]

Lo principal aqui es que entiendas que como vemos las llaves no tiene un nombre definido
sino que es un nombre general que nos permita introducir las llaves como los valores.
En esta forma es comodo, porque como vemos, tenemos tanto la llave en valores(de JSON) como en VALOR tambien en valores. y como vemos
Al llamarlo en python u otro lenguaje, si estamos haciendo un bucle o condicional vemos que si ponemos en una condicion la llave(de json) para sacar
el valor, simplemente es llamar a la llave que esta en un valor(de json), y asi poder sacar el VALOr que esta en otra llave(de JSON)
'''
# print('*' * 200 + '\n')
# print(datos['nombre'])
# print('*' * 200 + '\n')
# print(datos['idCursos'][23])
# print('*' * 200 + '\n')
# print(datos['cursos']['python'])


def cargandoDatos(ruta):

    # WITH(CONTEXTO9: Un contexto es basicamente establecer con una configuracion inicial y una final
    # para recuperar los valores anteriores, donde comunmente lo utilizamos para abrir los archivos con datos)
    # En este caso estamos estamos abriendo la variable para tener el contenido de la variable "ruta"
    # IMPORTANTE: SI OPEN NO TE FUNCIONE, MIRA QUE NO TENGAS UNA SUBCARPETA CON EL ARCHIVO DE
    # LO QUE HACE OPEN ES BUSCAR LA RUTA DESDE EL PRINCIPIO DE LA CARPETA, NO DESDE UNA UNA SUBCARPETA COMO TE IMAGINARAS
    # si lo pones
    with open(ruta) as contenido:

        # Estamos ocnvirtiendo el parametro que viene en la funcion a formato JSON
        # y como el parametro RUTa tiene la ruta con el nombre del archivo de JSON, entonces
        # no habria ningun problema
        # LOAD nos va retornar un "objeto" con el diccionario de JSON, es decir con LOAD
        # podremos llamar a las llaves del diccionario para sacar los valores con los datos
        profesor = json.load(contenido)

        print(profesor)

        otro = input("introduce papu: ")

        # print(profesor['cursos'])

        if otro == profesor["cursos"]:

            print("Hola")

        # print(profesor.get('nombre'))


if __name__ == "__main__":

    ruta = 'datos.json'

    cargandoDatos(ruta)
