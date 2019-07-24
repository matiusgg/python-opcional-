import random
import os

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def opcion1():

    

    # lista = random.randint(0, len(numeros) - 1)

    dificultad = 10

    opcion1 = random.randint(0, dificultad)

    

    return opcion1

def opcion2():

    
    dificultad = 25
    # lista = random.randint(0, len(numeros) - 1)

    opcion2 = random.randint(0, dificultad)

    

    return opcion2


def opcion3():

    dificultad = 50

    # lista = random.randint(0, len(numeros) - 1)

    opcion3 = random.randint(0, dificultad)

    

    return opcion3


def adivinaBucle(opciones, intentos):

    print(opciones)

    encontrar_numero = False

    contadorIntentos = 0

    # Mientras encontrar_numero no sea falso, hazme esto

    while not encontrar_numero:
        adivina = int(input('Adivina el numero: '))

    

        if adivina == opciones:
            print(f'Numero correcto, has adivinado el numero: {opciones:.2f}')
            encontrar_numero = True
        else:
            if opciones > adivina:
                os.system('cls')
                print(f'Mas alto aun no lo adivinas, el numero que ingresaste es: {adivina:.2f}')
                
                contadorIntentos +=1
                if contadorIntentos > intentos:
                    print('GAME oVER papu')
            # os.system('cls')
            if opciones < adivina:
                os.system('cls')
                print(f'Mas bajo aun no lo adivinas, el numero que ingresaste es: {adivina:.2f}')

                contadorIntentos +=1
                if contadorIntentos > intentos:
                    print('GAME oVER papu')



def Adivina():

    # OPCIONES: 1. 25 NUYM Y 10 VIDAS, 50 NUM Y 25 VIDAS, 10 NUM Y 5 VIDAS
    # 

    print('ESCOGE LA OPCION QUE QUIERAS ADIVINAR'.center(50, '*'))
    print('ADIVINA EL NUMERO Y 50\'000.000 DE EUROS')
    print('1.Numeros entre 0-10\n'
    '2.Numeros entre 0-25\n'
    '3.Numeros entre 0-50\n')

    dificultad = int(input('Escoge entre las opciones: '))

    if dificultad == 1:

        intentos1 = 5
        opcionPrimera = opcion1()

        print(opcionPrimera)

        adivinaBucle(opcionPrimera, intentos1)

    if dificultad == 2:

        intentos2 = 10
        opcionSegunda = opcion2()

        print(opcionSegunda)

        adivinaBucle(opcionSegunda, intentos2)

    if dificultad == 3:

        intentos3 = 25
        opcionTercera = opcion3()

        print(opcionTercera)

        adivinaBucle(opcionTercera, intentos3)
    



    

    # resultado = numeroAleatorio()

    

            # os.system('cls')
            # i = 0
            # while i == True:


            #     print(resultado)

            #     adivinaBucle = int(input('Adivina el numero'))

            #     i += 0


if __name__ == "__main__":
    Adivina()