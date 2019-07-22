'''
PALINDROMO: Una palabra que se puede leer al revez
'''

# funciones


def giro(palabra):

    # letra_invertida = []

    # for letra in palabra:
    #     # Aqui lo que pasa es que con isnert.() ponemos dentro la palabra del input, la cuestion aqui es que:
    #     # 1.String: El string de por si es una lista de caracteres, por lo cual el FOR con "i" con funcionara
    #     # 2.insert(): Entonces al usar insert() le indicaremos la posicion y el elemento de la lista que queremos meter,
    #     # que en este caso es el caracter del string que se pone en "letra". Por lo cual al momento de hacer la primera vuelta,
    #     # nos introduce el primer caracter del string en la posicion 0. Hasta aqui bien, al momento de hacer la 2 vuelta.
    #     # Coge el siguiente caracter del string y lo mete en la posicion 0, despejando a la posicion 1 la anterior letra, por lo cual
    #     # cada vez que hace una vuelta, cada caracter se va posicionando en el 0 nuevamente, lo que genera que al final tengamos la ultima letra
    #     # de un string en la posicion 0, mientras que la primera letra del string estara en la posisicion ultima porque fue arrastatrandose cada vez mas.
    #     # Ejm: ['r', 'o', 'm', 'a'] // AMOR
    #     letra_invertida.insert(0,letra)

    #     print(letra_invertida)

    # Otra forma

    palabraInvertida = palabra[::-1] # Nos volvea el elemento que tengamos

    if palabraInvertida == palabra:
        return True
        print(palabraInvertida)
    else:
        return False


def inicio():

    print('P A L I N D R O M O S')
    print(' ')


    palabra = str(input('Inserta la palabra: '))

    resultado = giro(palabra)

    if resultado == False:

        print('Es un palindromo')
    else:
        print('No es un polindromo')


if __name__ == "__main__":
    
    inicio()