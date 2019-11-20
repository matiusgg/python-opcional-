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

        #* iNTENTOS
        self.intentos = 0

        #* lista con letras Adivinadas
        self.listaAdivinado = []

        #* lista con los nombres de los archivos para imprimirlos en ahorcado.html cada vez que el usuario pierde
        self.listaImagenes = ['inicio', 'cabeza', 'torso', 'brazoderecho', 'brazoizquierdo', 'piernaderecha', 'pierdes']

    #********************************************************************

    def ahorcadito(self, inputLetra, activar, palabraRandom):

        print(palabraRandom)

        for i in palabraRandom:

            self.listaPalabra.append([i, ' | __ | '])
        
        if activar == 'activar':

            for i in self.listaPalabra:

                if inputLetra == i[0]:

                    i[1] = inputLetra

                    self.letrasCorrectas.append(inputLetra)

                    self.guardarLista(inputLetra)

                    print(i[1], end='')

            print(f'Letras correctas: {self.letrasCorrectas}')

            if len(self.letrasCorrectas) == 0:

                self.guardarLista(1)

                self.mostrarLista()

                if self.intentos == 7:

                    return self.listaPalabra, 'Has perdido, solo tenias 7 oportunidades'
                
                else:

                    return self.listaPalabra, self.listaImagenes[self.intentos]

            else:
                
                self.mostrarLista()

                print(self.listaPalabra)

                for i in self.listaPalabra:

                    self.listaAdivinado.append(i[1])

                if ' | __ | ' not in self.listaAdivinado:

                    return self.listaPalabra, 'Has ganado'

                else:

                    return self.listaPalabra, self.listaImagenes[self.intentos]


    # def random(self):

    #     return self.palabraRandom

    #**********************************************************

# * metodo guardarFrase()
    def guardarLista(self, lista):

        escribir = open('palabra.csv', 'a', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['lista'])

        salida.writerow([(lista)])

        # del salida
        escribir.close()

        #**********************************************************


    #***************************************************************

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

                    if row[0] == '1':

                        self.intentos += int(row[0])

                    print(f'Intentos Fallidos: {self.intentos}')

    
        


# objAhorcadito = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
# print(objAhorcadito.palabraRandom())

