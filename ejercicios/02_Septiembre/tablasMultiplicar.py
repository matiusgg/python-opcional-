def tabla():

    print('BIENVENIDO A TU SITIO PARA SABER LA TABLA DE MULTIPLICAR')
    print('')



    numero = int(input('Introduzca el numero que quiere:'))

    for i in range(11):

        multiplicar = numero * i

        print(f'{numero} * {i} = {multiplicar}')




if __name__ == "__main__":
    tabla()