# import random
# import os

# class Ahorcado():

#     SPRITES = [
#         '''
#      ---
#      |   |
#      0   |
#          |
#          |
#          |
#          ---------
#          ''',
#         '''
#      ---
#      |   |
#      0   |
#     /    |
#          |
#          |
#          ---------
#          ''',
#         '''
#      ---
#      |   |
#      0   |
#     /|   |
#          |
#          |
#          ---------
#          ''',
#         '''
#      ---
#      |   |
#      0   |
#     /|\  |
#          |
#          |
#          ---------
#          ''',
#         '''
#      ---
#      |   |
#      0   |
#     /|\  |
#      |   |
#          |
#          ---------
#          ''',
#         '''
#      ---
#      |   |
#      0   |
#     /|\  |
#      |   |
#     /    |
#          ---------
#          ''',
#         '''
#      ---
#      |   |
#      0   |
#     /|\  |
#      |   |
#     / \  |
#          ---------
#          '''
#     ]

#     def __init__(self):

#         self.palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

#         # * Lista donde vamos a agregar las letras que acierte el usuario.
#         self.letrasCorrectas = []

#         #* lista donde se agregara la palabra
#         self.listaPalabra = []

#         #* Palabra Random
#         self.palabraRandom = random.choice(self.palabras)

#     # *************************************************

#     # Metodo de busqueda

#     # ************************************************************

#     def ahorcadito(self):

#         intentos = 0

#         print(self.palabraRandom)

#         for i in self.palabraRandom:

#             self.listaPalabra.append([i, ' | __ | '])

#         while intentos < 10: 

#             inputLetra = input('Introduzca una letra: ')

#             if len(inputLetra) > 1:

#                 print('Debe introducir 1 letra')

#             else:

                
            
#                 for i in self.listaPalabra:

#                     if inputLetra == i[0]:

#                         i[1] = inputLetra

#                         # self.letrasCorrectas.append([i[1]])

#                         print(i[1], end='')

#                     else:

#                         print(i[1], end='')

                        

#             # for i in self.letrasCorrectas:

#             #     print(i, end='')

                

            

                


    


# objAhorcadito = Ahorcado()
# print(objAhorcadito.ahorcadito())