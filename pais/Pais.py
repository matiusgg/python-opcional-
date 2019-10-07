import json

class Pais():

    def __init__(self, pais):

        self.pais = pais

    def jsonPais(self, ruta):

        with open(ruta) as contenido:

            poblacion = json.load(contenido)

            for i in poblacion:

                if self.pais == i.get('country'):

                    return i.get('population')

#                 {

#     "Alemania": ["Alemania", 455454]

# }


# if self.pais == poblacion["Colombia"][0]:

#                 return poblacion["Colombia"][1]