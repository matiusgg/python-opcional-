import os
import random
import time

import recursos.recursos as recursos


class Juego():

    def __init__(self):

        self._piedra = False
        self._papel = False
        self._tijera = False
        self._sorpresa = False

    def Piedra(self, random):

        time.sleep(4)

        # print(recursos.opciones[1])

        piedra = recursos.opciones[1]

        if piedra == random:

            print(piedra, random)

            print('Has igualado, Vuelve a intentarlo')

        elif random == recursos.opciones[3]:

            print(piedra, random)

            print('Has ganado')

        elif random == recursos.opciones[2]:

            print(piedra, random)

            print('Has perdido')

    def Papel(self, random):

        time.sleep(4)1

        # print(recursos.opciones[2])

        papel = recursos.opciones[2]

        if papel == random:

            print(papel, random)

            print('Has igualado, Vuelve a intentarlo')

        elif random == recursos.opciones[3]:

            print(papel, random)

            print('Has perdido')

        elif random == recursos.opciones[1]:

            print(papel, random)

            print('Has ganado')

    def Tijera(self, random):

        time.sleep(4)

        # print(recursos.opciones[3])

        tijera = recursos.opciones[3]

        if tijera == random:

            print(tijera, random)

            print('Has igualado, Vuelve a intentarlo')

        elif random == recursos.opciones[2]:

            print(tijera, random)

            print('Has ganado')

        elif random == recursos.opciones[1]:

            print(tijera, random)

            print('Has perdido')

    def Sorpresa(self):

        time.sleep(4)

        print(recursos.opciones[4])


def run():

    juego1 = Juego()

    print('''
    
    
    
    ''')

    print('B I E N V E N I D O  A  NUESTRO JUEGO:'
          'PIEDRA, PAPEL O TIJERA'
          'ESCOGE TU MEJOR OPCION')

    while True:

        print('Has tu proximo lanzamiento')
        print('*************************')
        print('                 ')

        print('1.Piedra')
        print('2.Papel')
        print('3.Tijera')
        print('4.Bonus')
        print(' ')
        print('**************************')

        opcion = int(input('Tu proximo lanzamineto sera: '))

        aleatorio = random.choice(recursos.opciones)

        if opcion == 1:

            juego1.Piedra(aleatorio)

        elif opcion == 2:

            juego1.Papel(aleatorio)

        elif opcion == 3:

            juego1.Tijera(aleatorio)

        elif opcion == 4:

            juego1.Sorpresa()

        else:

            print('No has escogido ninguna opcion')

    os.system('cls')


if __name__ == "__main__":
    run()
