import random


class CambioImg():

    def __init__(self):


        self.montanyas = ['verde', 'azul', 'morado']

    def random(self, inputCambio):

        randomMontain = random.choice(self.montanyas)
        print(randomMontain)

        if inputCambio == 'activar':

            return randomMontain
        
        else:
            print('no es ACTIVAR')


# #* Objeto
# cambioObjt = CambioImg()
# cambioObjt.random('activar')



