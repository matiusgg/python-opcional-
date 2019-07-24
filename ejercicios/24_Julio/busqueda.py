import random
import os

# Algoritmo matematico para solucionar 
# 1. Crear unalista de numeros aleatorios de 50
# 2. ordenar la lista.
# 3. input para buscar numero
# 3. Aplicaar una busqueda binaria:
# 3.1. Coger el 1 y ultimo posicions de la lista, sumarlos, el resultado de la suma lo dividimos / 2. y nos dara un numero
# 3.2. este numero es la posicion donde esta el numero que queremos buscar, si no es igual, descartamos todos los elementos anteriores a esa posicion
# y volvemos a hacer la busqueda



def listaRandom(rango):

    listaAleatoria = []

    



    # No usamos la i, porque la i es del rango no de  la lista. SI USARIAMOS UN FOR


    while len(listaAleatoria) < rango:

        aleatorio = random.randint(0,200)

        listaAleatoria.append(aleatorio)

        cont = listaAleatoria.count(aleatorio)

        print(cont)

        if cont > 1:

            # Si El ultimo elemtno es el que provoco el duplicado por lo cual se elemina con el pop, no colocamos un APPEND otra vez
            # ya que si lo hacemos nos volvera a meter un nuevo numero aleatorio que posiblemente se volvera a repetir
            # entonces, en la siguiente vuelta del bucle se hace el append, por lo cual no nos preocupariamos 

            listaAleatoria.pop()



    listaAleatoria.sort()
    # print(listaAleatoria)

    suma = len(listaAleatoria) -1

    divicion = int(suma / 2)

    posicionNueva = listaAleatoria[divicion]

    return posicionNueva


      

# def inicio():


#     listaAleatoria = listaRandom(50)

#     print(listaAleatoria)

def busquedaBinaia(numeros, encontrarNueros, primeraPosicion, ultimaPosicion):

    if primeraPosicion > ultimaPosicion:
        return False

    
    medio = int((primeraPosicion + ultimaPosicion) / 2)

    if numeros[medio] == encontrarNueros:
        return True
    elif numeros[medio] > encontrarNueros:
        return busquedaBinaia(numeros, encontrarNueros, primeraPosicion, medio -1)
    else: 
        return busquedaBinaia(numeros, encontrarNueros, medio + 1, ultimaPosicion)







    

if __name__ == "__main__":
    listaRandom = listaRandom(50)

    encontrarNumero = int(input('Busca el numero'))

    resultado = busquedaBinaia(listaRandom, encontrarNumero, 0, len(listaRandom))

    if resultado is True:
        print('El numero SI esta en la Lista')

    else: print('El numero no esta en la lista')
