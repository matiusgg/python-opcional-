'''
SABER MANEJAR LOS ERRROES EN PYTHON:

1. AL momento
'''

'''
TRY: 
'''

# si sale un error

# TRY: Nos permite adelantarnos a unm error, es decir podemos manejar/controlando como sera el error dentro de un bucle o condicional y poder evitarlo,
# en donde en el TRY se pondra que "INTENTE" hacer lo que le indiquemos dentro de el, si va a ver un error, que vaya al EXCEPT
try:
    print(poblaciones[pregunta])

# EXCEPT: En el EXCEPT, le indicamos que si nos sale el error si no nos dio el TRY, nos ponga lo que le pongamos dentro del EXCEPT, por ejemplo aqui un print
# En este ejemplo con el ejercicoi de POBLACION, si no hay llaves que coincidan con el INPUt, lanzanos en EXCEPT el mensaje del print, en vez de que nos salga todo un error de la consola
except KeyError:
    print(f'No tenemos los datos de{pregunta.title()}')