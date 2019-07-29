# detectar cual es el primer caracter que no se repite, la cadena de caracteres e pone mediante un input

def caracteres(cadena):

    for i in cadena:

        contarcadena = cadena.count(i)

        cadenaLista = list(cadena)

        longitud = len(cadenaLista)


        print(contarcadena)

        if contarcadena == 2:

            print('Hay mas de uno repetido')

            caracterRepetido = []

            caracterRepetido.append(i)

            print(f'El primer caracter que se repite es: {caracterRepetido[0]}')

            break

        if contarcadena == longitud:

            print('Todas las letras se repiten')

            break

        
        else:
            print(i)

            primerCaracter = []

            primerCaracter.append(i)

            print(primerCaracter)

            print(f'El primer caracter que se encontro que no se repite fue: {primerCaracter[0]}')

            break



def run():

    print('DESCUBRE CUAL ES EL CARACTER QUE NO SE REPITE:\n')
    print('ESCRIBE EL CADENA DE CARACTERES.\n')

    cadena = str(input('Cadena de texto:'))

    caracteres(cadena)
    

if __name__ == "__main__":
    run()


# COMO LO HIZO EL PROFE

# def primer_caracter(secuencia):
#     for i in secuencia:

#         if secuencia.count(i) > 1:
#             continue
#         else:
#             return i

#     # Ale star el return FALSE fuera del FOR por la tabulacion donde tneemos la primera letra que no se repite,
#     # le estamos indicando que si no nos retorna el "i" del condicional ELSE, etnoces que nos retorne FALSE, es deicr
#     # que nos retorne un return u otro, no ambos.

#     return False

# if __name__ == "__main__":

#     secuencia = 'zzzzzhzzzzzz'

#     resultado = primer_caracter(secuencia)

#     if resultado == False:
#         print('Todos los caracteres de la cadena se repite')
#     else:
#         print(f'El primer caracter no repetido es: {resultado}')