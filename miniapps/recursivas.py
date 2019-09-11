"""

 recursivas

"""


def jugar(intento=1):

    respuesta = input('De que color es una naraja: ')

    if respuesta != 'naranja':

        if intento < 3:

            print('\n Fallaste: Te ries del juego? Nosotros de tu **** madre. AVE MARIA CUANDO SERAS MIA!!!!!!!!!!!!!!!!!!!!!!')

            intento += 1

            # RECURSIVIDAD: LLAMAR UNA FUNCION DENTRO DE OTRA FUNCION, ESTO SERIA COMO UN BUCLE. SON BUENAS EN MOMENTO PUNTUALES,
            # PERO NO ES RECOMENDABLE

            jugar(intento)

        else:
            print('\n Ganaste Crack. pero tampoco te vengas muy arriba CRACK')

    else:
        print('ganaste, que quieres que haga?')


jugar()
