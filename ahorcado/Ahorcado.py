'''
AHORCADITO
'''

import pymysql
import random
import os
import csv


class Ahorcado():

    def __init__(self, localhost, usuario, password, basedeDatos):

        self.conexion = pymysql.connect(localhost, user=usuario, password=password, db=basedeDatos)

        self.palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

        # * Lista donde vamos a agregar las letras que acierte el usuario.
        self.letrasCorrectas = []

        #* lista donde se agregara la palabra
        self.listaPalabra = []

        #* Palabra Random
        self.palabraRandom = random.choice(self.palabras)

        #* iNTENTOS que tambien funciona como fallos
        self.intentos = 0

        #* Aciertos
        self.aciertos = 0

        #* lista con letras Adivinadas
        self.listaAdivinado = []

        #* lista con los nombres de los archivos para imprimirlos en ahorcado.html cada vez que el usuario pierde
        self.listaImagenes = ['inicio', 'cabeza', 'torso', 'brazoderecho', 'brazoizquierdo', 'piernaderecha', 'pierdes']

        #* Aciertos lista
        self.aciertosLista = []

        #* RECORD
        self.record = 0

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

                #* SELF.MOSTRARLISTA() tiene el # de intentos y aciertos, por lo cual podemos usarlo en los
                #* condicionales sin que cambien.
                self.mostrarLista()

                if self.intentos == 7:

                    return self.listaPalabra, 'Has perdido, solo tenias 7 oportunidades', self.aciertos, self.intentos, self.record
                
                else:

                    return self.listaPalabra, self.listaImagenes[self.intentos], self.aciertos, self.intentos, self.record

            else:
                
                self.mostrarLista()

                print(self.listaPalabra)

                for i in self.listaPalabra:

                    self.listaAdivinado.append(i[1])

                if ' | __ | ' not in self.listaAdivinado:

                    self.record += 1

                    return self.listaPalabra, 'Has ganado', self.aciertos, self.intentos, self.record

                else:

                    return self.listaPalabra, self.listaImagenes[self.intentos], self.aciertos, self.intentos, self.record


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
                    else:



                        for i in self.listaPalabra:

                            if row[0] == i[0]:

                                self.aciertosLista.append(row[0])

                                if self.aciertosLista.count(row[0]) > 1:

                                    print('Hay letras repetidas')

                                else:

                                    self.aciertos += 1

                                

                        print('lista con las letras correctas del csv: ')
                        print(self.aciertosLista)

                        print('Aciertos: ' + str(self.aciertos))

                        

                                

                    print(f'Intentos Fallidos: {self.intentos}')

        # Metodo de busqueda

    def query(self, sql):

        with self.conexion.cursor() as cursor:

            cursor.execute(sql)

            self.conexion.commit()

            self.conexion.close()

            return cursor.fetchall()


# objAhorcadito = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
# print(objAhorcadito.palabraRandom())

