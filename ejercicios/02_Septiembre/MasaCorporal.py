

def datos():

    peso = float(input('Introduzca el peso: '))
    altura = float(input('Introduzca el altura: '))

    # POW = permite elevar un numero colocando el exponenete que queramos donde pow(numero, numero de exponente)

    # pow(altura, 2)

    imc = peso / (altura**2)

    # ROUND: Que nos redondea el resultado, donde round(numero que uqeremos redondear, numero de decimales)

    total = round(imc, 2)

    print(f'Tu Indice de masa corporal es: {total}')






def masaCorporal():

    print('BIENVENIDO A TU SITIO PARA DESCUBRIR TU MASA CORPORAL')
    print('1.KG & METROS')
    print('2.LB & PULGADAS')

    conversion = int(input('Introduzca que la conversion que quiere:'))

    if conversion == 1:

        datos()
    else:
        print('No has escogido ninguna opcion')




if __name__ == "__main__":
    masaCorporal()