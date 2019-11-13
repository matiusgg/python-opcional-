'''
AHORCADITO
'''

import pymysql
import random
import os

class Ahorcado():

    SPRITES = [
'''
     ---
     |   |
     0   |
         |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /    |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|   |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
     |   |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
     |   |
    /    |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
     |   |
    / \  |
         ---------
         '''
]

    def __init__(self, localhost, usuario, password, basedeDatos):

        self.conexion = pymysql.connect(localhost, user=usuario, password=password, db=basedeDatos)

        #* Lista donde vamos a agregar las letras que acierte el usuario.
        self.letrasCorrectas = []

    #*************************************************

    # Metodo de busqueda

    def query(self, sql):

        with self.conexion.cursor() as cursor:

            cursor.execute(sql)

            self.conexion.commit()

            self.conexion.close()

            return cursor.fetchall()

    #*****************************************************

    def palabraRandom(self):

        with self.conexion.cursor() as cursor:

            sqlPalabras = 'SELECT palabra FROM palabras'

            cursor.execute(sqlPalabras)

            self.conexion.commit()

            self.conexion.close()

            palabrasSQL = cursor.fetchall()

            #* Lista para guardar las palabras 
            listaPalabras = []

            print(palabrasSQL)

            for i in palabrasSQL:

                print(i[0])
                listaPalabras.append(i[0])
            
            print(listaPalabras)

            palabraRandom = random.choice(listaPalabras)

            return palabraRandom

    #************************************************************

    def ahorcadito(self, inputLetra):

        for letra in self.palabraRandom():

            if inputLetra == letra:

                self.letrasCorrectas.append(inputLetra)

# objAhorcadito = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
# print(objAhorcadito.palabraRandom())

# import random
# import os
# SPRITES = [
# '''
#      ---
#      |   |
#      0   |
#          |
#          |
#          |
#          ---------
#          ''',
# '''
#      ---
#      |   |
#      0   |
#     /    |
#          |
#          |
#          ---------
#          ''',
# '''
#      ---
#      |   |
#      0   |
#     /|   |
#          |
#          |
#          ---------
#          ''',
# '''
#      ---
#      |   |
#      0   |
#     /|\  |
#          |
#          |
#          ---------
#          ''',
# '''
#      ---
#      |   |
#      0   |
#     /|\  |
#      |   |
#          |
#          ---------
#          ''',
# '''
#      ---
#      |   |
#      0   |
#     /|\  |
#      |   |
#     /    |
#          ---------
#          ''',
# '''
#      ---
#      |   |
#      0   |
#     /|\  |
#      |   |
#     / \  |
#          ---------
#          '''
# ]
# PACKINICIO = [
#    'COCODRILO',
#    'AMANTE',
#    'DISLEXIA',
#    'AMFIBIO',
#    'SENTIMIENTO',
#    'DIAZEPAN',
#    'SIFILIS'
# ]
# def palabraAleatoria():
#    lista = random.randint(1, len(PACKINICIO) -1)
#    palabra_oculta = str(PACKINICIO[lista])
#    return palabra_oculta
# def run():
#    palabraOK = palabraAleatoria()
#    ocultar = ['__'] * len(palabraOK)
#    intentos = 0
#    while True:
#        print('')
#        tablero(ocultar, intentos)
#        caracter = str(input('DISPARA UNA LETRA: '))
#        indexarLetra = []
#        for i in range(len(palabraOK)):
#            if palabraOK[i] == caracter:
#                indexarLetra.append(i)
#                print(indexarLetra)
#        if len(indexarLetra) == 0:
#            intentos += 1
#        if intentos == 7:
#            print('')
#            print(f'¡Perdiste! La palabra correcta es: {palabraOK} ')
#            break
#        else:
#            for i in indexarLetra:
#                ocultar[i] = caracter
#        try:
#            ocultar.index('__')
#        except ValueError:
#            print('')
#            print(f'Felicidades! Se ha salvado!')
#            break
# def tablero(ocultar,intentos):
#    # os.system('clear')
#    print('TIENES TU OPORTUNIDAD PARA MATAR AL NEGRO')
#    print('----------------------------------------')
#    print('')
#    print(SPRITES[0])
#    print('')
#    print(ocultar)
#    print('----------------------------------------')
# if __name__ == "__main__":
#    run()