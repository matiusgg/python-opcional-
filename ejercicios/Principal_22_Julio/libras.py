# CALCULADORA DE DIVISAS: que nos haga las LIBRAs -> euros

# Funciones qu epondramos en el MAIN. En las funciones da completamente igual si el codigo se crea antes o despues, ya que al cargars en memoria
# con el MAIN no da problemas

def inicio():

    pregunta = float(input('Que conversion quieres? 1.libra 2.euros: '))

    if pregunta == 1:
        libra()

    if pregunta == 2:
        euro()
    
    else:
        print('No has escogido una opcion')


def libra():

    dinero = float(input('Introduce la cantidad de libra -> euro:'))

    if dinero != 0:
        dinero *= 1.1125
        print(f'Conversion a euros es: {dinero:.2f}')


def euro():

    dinero = float(input('Introduce la cantidad de euro -> libra:'))

    if dinero != 0:
        dinero *= 0.90
        print(f'Conversion a libras es: {dinero:.2f}')



# Ahora hacemos el MAIN, para dar a entender el inicio del codigo

if __name__ == "__main__":
    inicio()