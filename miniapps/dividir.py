"""

"""


def divide(num1, num2):

    division = num1 / num2

    # en el caso de que la divion sea por 0, nos dara infinito y por lo tanto un error. Para manejar los errores recordemos
    # que podemos usar TRY

    try:

        return division

    # De donde sale ZeroDividionError, es el nombre del error que te dio en la consola, por lo cual cuando te da un error en la consola
    # te saldra el nombre y de ahi lo copias
    # Aqui lo que hacemos es cambiaR todo el error por lo que pongamos dentro de except, en este caso unos print's, pero que nos ganamos con esto?.
    # Simple, nos permite manejar ese error y para que no nos detenga el resto de aplicacion, es decir que aunque halla el eror el resto de la aplicacion
    # no se detenga si es que tienes mas cosas

    except ZeroDivisionError:
        print('No se puede dividir entre 0, CRACK. vete pa tu casa hombre')
        return 'Operacion Errónea'


if __name__ == "__main__":

    num1 = float(input('num:1 '))
    num2 = float(input('num:2 '))

    print(divide(num1, num2))
