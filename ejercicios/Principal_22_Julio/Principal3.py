import palindromo
import primos
import libras

def inicio():

    print('Bienvenido a nuestra app basica. EScoge la opcion\n'
    '1.Palindromo\n'
    '2.Primo\n'
    '3.Libras\n')

    opcion = str(input('Escoge la Opcion: '))

    if opcion == '1':

        palindromo.inicio()
    
    if opcion == '2':

        primos.primos()
    
    if opcion == '3':

        libras.inicio()
    
    else:
        print('No escogiste ninguna opcion')



if __name__ == "__main__":
    inicio()