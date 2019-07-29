'''
BUCLES:
El WHILE en python es mas generico que el FOR
'''

'''
CONTINUE: Si tenemos un condicional y le ponemos un CONTINUE, si estya condicional se cumple el CONTINUE lo que hara, es pasar a la siguiente vuelta,
mientras que si no se cumple la condicion hazme el codigo que tenga o los siguientes condicionales

BREAK: Rompe un bucle y no sigue los siguientes condicionales como tampoco las siguientes vueltas
'''

# WHILE

import math

# EJEMPLO: 

for i in range(20):
    if i != 5:
        continue
    else:
        print(i)

        # Lo que nos hara es que si la condicion se cumple el CONTINUE no nos hara el print del ELSE y pasara a la siguiente vuelta,
        # mientras que si es FALSe la condicions si nos hace el print del ELSE

numero = int(input('Escribe un numero: '))

# El bucle comprueba con la condicion si el numero es negativo

# si es asi, itera el contenido.
# y si no se cumple la condiocn pasa a la siguiente linea.
# La identacion/tabulaciones jerarquia siguen como en los condicionales

while numero < 0:
    print('error, debe escribir un numero positivo')
    # Lo ue nos hace el input en este caso es para el bucle infinito que se haria si no lo pararamos con algo
    numero = float(input('EScribe un numero de nuevo CRACK: '))

# este print ya no pertenece al while, por la tabulacion RECUERDA

print(f'\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}')

# While con variable iteradora $i(php). El $i++ seria en PYTHON es i += 1

# CONTROL + C

i = 0

while i < 5:
    print('Hola mundo')
    i += 1

print('Final')

# for: Es el bucle que se utliza en las colecciones(tupla, filas, diccionario, conjunto) de datos. Nos mostrara con print los elementos de la coleccion
# en IN en el FOR lo que hace es igual i con la coleccion uno por unbo, es decir, i = elemento-> imprime, i = elemento-> imprime, y asi sucesivamente
# Donde la lista con IN, nos ira ontroduciendo un elemento po vuelta dentro de "i"
for i in [1,2,3,4,5,6]:
    # imprmimos i para mostrar los elementos
    print(i) 

# pero si queremos otro codigo en el for obviamente podemos poner cualquier codigo, la cuestion aqui
# es que la variable i se iguala con cada elemento de la coleccion y segun la cantidad que tenga esa coleccion
# sera el numero de bucles que nos hara el FOR
# por ejemplo SALIR, nos mostrara SAlir * la cantidad de elementos que tiene esa coleccion

for i in [1,2,3,4,5,6]:
    # imprmimos i para mostrar los elementos
    print('SALIR') 

# Ahora sin necesidad de poner los elementos de la coleccion sino la variable que los tiene

coleccion01 = (1,2,3,4,5,6)

for i in coleccion01:

    print(f'Elemento: {i}')

coleccion02 = {

    'Pepe': 34,
    'Maria': 23
}

# Al hacerle el FOr a un Diccionario la i se igualara con la llave, por lo cual si no usamos nombreDelDiccionario[]
# para especificar que con i queremos que nos saque los valores de las llaves

for i in coleccion02:
    print(f'{i} -> {coleccion02[i]}')

    
# Otra forma: usando la funcion items que agrupa tanto la llave como el valor, en donde
# la variable llave agrupa las LLAVEs del diccionario mientras que el valor agrupa los VALORES del diccionario
# como lo sabe?, las variables llave y valor serian los i del FOR, la cuestion es que ITEMS() los agrupa en ambos


for llave, valor in coleccion02.items():

    print(f'{llave} -> {valor}')


#Bucle con cada caracter de un string. Hacer un STRIng es ya en si misma un a coleccion de caracteres
# por lo cual es como si cada caracter fuera un elemento de una coleecion por lo cual en el FOR
# imprimira cada caracter uno por uno

coleccion03 = 'Hola Mundo'

for i in coleccion03:
    print(i)


# END: nos permite concatenar los elementos, es decir, al momento de hacer el bucle no nos lo imprime
# hacia abajo si no en una sola linea.


for i in coleccion03:
    print(f'{i}', end:'')


