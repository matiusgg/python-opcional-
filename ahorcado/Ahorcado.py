'''
AHORCADITO
'''

import pymysql
import random
import os
import csv


class Ahorcado():

    def __init__(self):

        self.palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

        # * Lista donde vamos a agregar las letras que acierte el usuario.
        self.letrasCorrectas = []

        #* lista donde se agregara la palabra
        self.listaPalabra = []

        #* Palabra Random
        self.palabraRandom = random.choice(self.palabras)

    def ahorcadito(self, inputLetra, activar, palabraRandom):

        print(palabraRandom)

        for i in palabraRandom:

            self.listaPalabra.append([i, ' | __ | '])
        
        if activar == 'activar':



            for i in self.listaPalabra:

                if inputLetra == i[0]:

                    i[1] = inputLetra


                    self.guardarLista(inputLetra)

                    print(i[1], end='')

                else:

                    print(i[1], end='')

                    

            self.mostrarLista()

            print(self.listaPalabra)

            return self.listaPalabra


    # def random(self):

    #     return self.palabraRandom

# * metodo guardarFrase()
    def guardarLista(self, lista):

        escribir = open('palabra.csv', 'a', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['lista'])

        salida.writerow([(lista)])

        # del salida
        escribir.close()

    # * metodo mostrarFrase()
    def mostrarLista(self):

        with open('palabra.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

                if row[0] != 'lista':

                    for i in self.listaPalabra:

                        if row[0] == i[0]:

                            i[1] = row[0]

                    




# objAhorcadito = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
# print(objAhorcadito.palabraRandom())

