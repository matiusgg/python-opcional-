'''
AHORCADITO
'''

import pymysql
import random
import os


class Ahorcado():

    def __init__(self):

        self.palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

        # * Lista donde vamos a agregar las letras que acierte el usuario.
        self.letrasCorrectas = []

        #* lista donde se agregara la palabra
        self.listaPalabra = []

        #* Palabra Random
        self.palabraRandom = random.choice(self.palabras)

    def ahorcadito(self, inputLetra, activar):

        if activar == 'activar':

            print(self.palabraRandom)

            for i in self.palabraRandom:

                self.listaPalabra.append([i, ' | __ | '])


            if len(inputLetra) > 1:

                print('Debe introducir 1 letra')

            else:


                for i in self.listaPalabra:

                    if inputLetra == i[0]:

                        i[1] = inputLetra

                        self.letrasCorrectas.append([i[1]])

                        print(i[1], end='')

                        return self.letrasCorrectas

                else:

                    print(i[1], end='')

                    return self.letrasCorrectas


    def random(self):

        return self.palabraRandom


#     def __init__(self, localhost, usuario, password, basedeDatos):

#         self.conexion = pymysql.connect(
#             localhost, user=usuario, password=password, db=basedeDatos)

#         # * Lista donde vamos a agregar las letras que acierte el usuario.
#         self.letrasCorrectas = []

#     # *************************************************

#     # Metodo de busqueda

#     def query(self, sql):

#         with self.conexion.cursor() as cursor:

#             cursor.execute(sql)

#             self.conexion.commit()

#             self.conexion.close()

#             return cursor.fetchall()

#     # *****************************************************

#     def palabraRandom(self):

#         with self.conexion.cursor() as cursor:

#             sqlPalabras = 'SELECT palabra FROM palabras'

#             cursor.execute(sqlPalabras)

#             self.conexion.commit()

#             self.conexion.close()

#             palabrasSQL = cursor.fetchall()

#             # * Lista para guardar las palabras
#             listaPalabras = []

#             print(palabrasSQL)

#             for i in palabrasSQL:

#                 print(i[0])
#                 listaPalabras.append(i[0])

#             print(listaPalabras)

#             palabraRandom = random.choice(listaPalabras)

#             return palabraRandom

#     # ************************************************************

#     def ahorcadito(self, inputLetra):

#         for letra in self.palabraRandom():

#             if inputLetra == letra:

#                 self.letrasCorrectas.append(inputLetra)


# objAhorcadito = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
# print(objAhorcadito.palabraRandom())

