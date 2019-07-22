#Funciones
# SPRITe: ES un fotograma de una pelicula, como animacion 

import random
import os

SPRITES = [
   '''
        *---*
        |   |
            |
            |
            |
            |
            |
            |
            *-----* ''','''
        *---*
        |   |
        O   |
        |   |
            |
            |
            |
            |
            *-----* ''','''
        *---*
        |   |
        O   |
       /|   |
            |
            |
            |
            |
            *-----* ''','''
        *---*
        |   |
        O   |
       /|\  |
            |
            |
            |
            |
            *-----* ''','''
        *---*
        |   |
        O   |
       /|\  |
        |   |
            |
            |
            |
            *-----* ''','''
        *---*
        |   |
        O   |
       /|\  |
        |   |
       /    |
            |
            |
            *-----* ''','''

        *---*
        |   |
        O   |
       /|\  |
        |   |
       /\   |
            |
 MUERTE     |
            *-----* '''

]

PACK = [
    'playas',
    'sobresadas',
    'ensaimadas'
]

# randomLista = random.choice(lista)



def PalabraRandom():

    # El -1 es porque nos empieza a contar desde 1 y nosdara error porque la cantdad empieza desde 0

    lista = random.randint(0, len(PACK) - 1)

    return PACK[lista]


    # print(randomLista)

    # letras = []

    # os.system('clear') # cada vez que se pida un input se va a limpiar la pantalla

    # for i in randomLista:

    #     letras.append(i)

    #     print(letras)


def tablero(ocultar, intentos):

    #Limpiar la terminal y solo ver la aplicacion

    os.system('clear')

    print(' QUIERES JUGAR A UN JUEGO')

    print('--------------------------------------------------------')

    # Impresion general del ahorcado, aun no empieza el juego

    print(SPRITES[0])

    
    print(ocultar)

    print(f'Intentos: {intentos}')


            

# def inputs(resultado):

#     # ocultar = ['_'] * len(resultado)

#     for i in resultado:
#         ponerLetra = str(input(f'_'))

#         if ponerLetra in i:
#         #    print(ocultar)
#             print('Letra Correcta')

#         else:
#             # print(ocultar)
#             print('Letra incorrecta')





    



def run():

    #Limpiar la terminal y solo ver la aplicacion

    # os.system('clear')


    

   

    resultado = PalabraRandom()

    # Creacion espacios de caracteres

    ocultar = ['_'] * len(resultado)


    # # Impresion
    # print(ocultar)

        # Intentos

    intentos = 0

    

    print(f'{resultado}')

    # Preguntar por caracter

    i = 0

    while i < len(resultado):

        
        print('')

        tablero(ocultar, intentos)

        
        caracter = str(input('Pon el caracter: '))


        i += 1
    
    # LOGICa del JUEGO

    indexarLetra = []

    for i in range(len(resultado)):

        if resultado[i] == caracter:

            indexarLetra.append(i)

            print(indexarLetra)
    
        if len(indexarLetra) == 0:
            intentos += 1

            if intentos == 10:
                print('Game over. Vuelve a intentarlo')
                break
        else:
            for i in indexarLetra:
                ocultar[i] = caracter
        
        # Ganar

        try:
            ocultar.index('_')
        # Evaluamos si tiene error dentro del TRY

        except ValueError:

            print('')

        


    


    # inputs(resultado)


if __name__ == "__main__":
    run()