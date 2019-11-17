import random
import os

# listaPalabra = []

# palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

# palabraRandom = random.choice(palabras)

# letrasCorrectas = []


# def ahorcadito(palabraRandom, inputLetra):

#     print(palabraRandom)

#     for i in palabraRandom:

#         listaPalabra.append([i, ' | __ | '])


#         if len(inputLetra) > 1:

#             print('Debe introducir 1 letra')

#         else:


#             for i in listaPalabra:

#                 if inputLetra == i[0]:

#                     i[1] = inputLetra

#                     letrasCorrectas.append([i[1]])

#                     print(i[1], end='')

#                     # return letrasCorrectas

#             else:

#                 print(i[1], end='')

#                 # return letrasCorrectas

            
# if __name__ == "__main__":
    
#     i = 0

#     while i < 10:

#         usuario = input('Introduzca la letra: ')

#         ahorcadito(palabraRandom, usuario)

#         i += 1

class Ahorcado():



    def __init__(self):

        self.palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

        # * Lista donde vamos a agregar las letras que acierte el usuario.
        self.letrasCorrectas = []

        #* lista donde se agregara la palabra
        self.listaPalabra = []

        #* Palabra Random
        self.palabraRandom = random.choice(self.palabras)

    # *************************************************

    # Metodo de busqueda

    # ************************************************************

    def ahorcadito(self):

        intentos = 0

        print(self.palabraRandom)

        for i in self.palabraRandom:

            self.listaPalabra.append([i, ' | __ | '])

        print(f'join: ')
        joinnuevo = ''.join(self.listaPalabra[0])
        print(joinnuevo)

        while intentos < 10: 

            inputLetra = input('Introduzca una letra: ')

            if len(inputLetra) > 1:

                print('Debe introducir 1 letra')

            else:

                
            
                for i in self.listaPalabra:

                    if inputLetra == i[0]:

                        i[1] = inputLetra

                        self.letrasCorrectas.append(i[1])

                        print(i[1], end='')

                    else:

                        print(i[1], end='')

                        self.letrasCorrectas.append(i[1])

            intentos += 1

        

        print(f'letrasCorrectas: {self.letrasCorrectas}')

            # for i in self.letrasCorrectas:

            #     print(i, end='')

                

            

                


    


objAhorcadito = Ahorcado()
print(objAhorcadito.ahorcadito())