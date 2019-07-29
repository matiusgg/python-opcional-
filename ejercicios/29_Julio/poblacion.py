
# Crear 


def Muestrapoblaciones(poblacion, poblaciones):


    vocales = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ò': 'o',
        'ñ': 'ny'
    }

    # for llave, valor in poblaciones.items():

        # print(f'No tenemos los datos de{pregunta.title()}')


    
    
    try:
        # El ENCODE('ascii) verifica si los caracteres estan en la tabla ASCII de EEUU, si no lo estan, que seria el caso de que tengan tildes
        # ira al EXCEPT.
        poblacion.encode('ascii')
    except UnicodeEncodeError:
        print('Nombre de población con acentos')

        # for i in range(len(pregunta) -1):
        for llave, valor in vocales.items():

                # REPLACE: NOs permite reemplazar un elemento por otro omo si hicieramos un CONTROL + F, si tenemos un diccionario
                # de vocales y queremos reemplazar una vocal por ejemplo por otra, el REPLACE ira buscando en el diccionario cual vocalKEY coincide con
                # alguna vocal de la palabra del input y asi reemplazarla con VALOR de la KEY.

            texto = poblacion.replace(llave, valor)

    return texto
            

def insertar(poblaciones):

    print(' INSERTA UN NUEVA POBLACION:')

    nueva = str(input('Introduce la nueva poblacion: ')).lower()

    numeroPoblacion = int(input('Introduce la cantidad de poblacion:'))

    poblaciones[nueva] = numeroPoblacion



def run():

    poblaciones = {
        'manacor': 40.279,
        'palma': 402.949,
        'sòller': 13.791,
        'valldemossa' : 2.003,
        'inca': 30.944,
        'llucmajor' : 35.057
    }


    print('descubre que poblacion tiene tu PUEBLO/CIUDAD/PAIS:\n')
    print('ESCOGE ENTRE LAS OPCIONES:')
    print('1. POBLACION')
    print('2. Agrega una nueva poblacion')
    print('3. Salir')
    
    # bucle infinito

    # while True:

    opciones = int(input('Introuce la opcion: '))

    if opciones == 1:
        
        palabra = str(input('Introuce la poblacion: ')).lower()

        Muestrapoblaciones(palabra, poblaciones)
    
    if opciones == 2:

        insertar(poblaciones)

        print(poblaciones)
    
    if opciones == 3:

        print('Has salido del buscador de poblacion')







# Como lo hizo toni en el RUN():

# while True:
#     pregunta = str(input('Poblacion de mallorca, para salir \"salir\": ')).lower()

#     if pregunta == 'salir':

#         break

#     else:

#         #Basicamente al poner pregunta dentro de [] del diccionarios de poblaciones, este como en un array llave-valor,
#         # Buscaraa mediante la llave si esta coincide con la poblacion del input, y nos dara elvalor.

#         print(poblaciones[pregunta])

'''
SABER MANEJAR LOS ERRROES EN PYTHON:

1. AL momento
'''

# si sale un error

# TRY: Nos permite adelantarnos a unm error, es decir podemos manejar/controlando como sera el error dentro de un bucle o condicional y poder evitarlo,
# en donde en el TRY se pondra que "INTENTE" hacer lo que le indiquemos dentro de el, si va a ver un error, que vaya al EXCEPT
# try:
#     print(poblaciones[pregunta])

# # EXCEPT: En el EXCEPT, le indicamos que si nos sale el error si no nos dio el TRY, nos ponga lo que le pongamos dentro del EXCEPT, por ejemplo aqui un print
# # En este ejemplo con el ejercicoi de POBLACION, si no hay llaves que coincidan con el INPUt, lanzanos en EXCEPT el mensaje del print, en vez de que nos salga todo un error de la consola
# except KeyError:
#     print(f'No tenemos los datos de{pregunta.title()}')


if __name__ == "__main__":
    run()
