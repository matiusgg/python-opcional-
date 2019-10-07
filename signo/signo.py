import json

animales = ['Mono', 'Gallo', 'Perro', 'Cerdo',
            'Rata', 'Buey', 'Tigre', 'Conejo', 'Dragon', 'Serpiente', 'Caballo', 'Cabra']


class HoroscopoChino():

    ANIMALES = ['mono', 'gallo', 'perro', 'jabali', 'rata', 'buey',
                'tigre', 'conejo', 'dragon', 'serpiente', 'caballo', 'oveja']

    def __init__(self, anyo_usuario):

        self.anyo_usuario = anyo_usuario

    def signo(self):
        try:

            for i in range(0, 12):

                if self.anyo_usuario % 12 == i:

                    global animal

                    animal = self.ANIMALES[i]

                    return animal

        except ValueError:
            print('Error, vuelve a intentarlo')
            signo()

    def compatibilidad(self):

         with open('static/json/descripcion.json') as contenido:

            descripcion = json.load(contenido)

            animalEscogido = animal

            for i in descripcion:

                if animalEscogido == i.get('animal'):

                    return i.get('compatibilidad')

    def descripcion(self):

        with open('static/json/descripcion.json') as contenido:

            descripcion = json.load(contenido)

            animalEscogido = animal

            for i in descripcion:

                if animalEscogido == i.get('animal'):

                    return i.get('descripcion')
