

animales = ['Mono', 'Gallo', 'Perro', 'Cerdo',
            'Rata', 'Buey', 'Tigre', 'Conejo', 'Dragon', 'Serpiente', 'Caballo', 'Cabra']


class HoroscopoChino():

    ANIMALES = ['Mono', 'Gallo', 'Perro', 'Cerdo', 'Rata', 'Buey',
                'Tigre', 'Conejo', 'Dragon', 'Serpiente', 'Caballo', 'Oveja']

    def __init__(self, anyo_usuario):

        self.anyo_usuario = anyo_usuario

    def signo(self):
        try:

            for i in range(0, 12):

                if self.anyo_usuario % 12 == i:

                    return self.ANIMALES[i]

        except ValueError:
            print('Error, vuelve a intentarlo')
            signo()


