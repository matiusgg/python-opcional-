

# clase-padre
class vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

        # PORQUE DEFINIMOS LAS PROPIEDADES DENTRO DEL CONSTRUCTOR Y NO AFUERA DE ESTE?
        # PORQUE NOS BENEFICIA AL MOEMNTO DE CREAR UN OBJETO, YA QUE ES MAS ACCESIBLE
        # PORQUE CUANDO SE CREA EL OBJETO LAS TENEWMOS DISPONIBLES MIENTRAS QUE SI LAS DEFINIMOS
        # AFUERA NO HABRIA PROBLEMA TAMPOCO
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelerar = True

    def frenar(self):

        self.frenar = True

    def estado(self):

        print(f'Marca: {self.marca} \n Modelo: {self.modelo} \n En marcha: {self.enmarcha} \n'
              f'Acelerar: {self.acelerar} \n Frenar: {self.frenar} \n')


# como vemos se herera simplemente colocando la clase-padre entre parentesis al momento
# de crear la subclase.
class Moto(vehiculos):

    caballito = ''

    def caballitos(self):

        self.caballito = 'Estoy haciendo un caballito!!'

        return self.caballito

    # Sobreescribimos el metodo, ya que queremos que la propiedad caballito se incluye en el metodo
    # heredado por el padre, la cual es ESTADO

    def estado(self):

        print(f'Marca: {self.marca} \n Modelo: {self.modelo} \n En marcha: {self.enmarcha} \n '
              f'Acelerar: {self.acelerar} \n Frenar: {self.frenar} \n Caballito: {self.caballitos()}')


class Furgoneta(vehiculos):

    def carga(self, carga):

        self.carga = carga

        if(self.carga):

            return 'Furgoneta cargada hasta arriba'

        else:

            return 'Furgoneta no cargada'


# ****** VEHICULOS ELECTRICOS **********

# *CLASE-PADRE PARA LOS OBJETOS CON ELECTRICIDAD

class VELectricidad(vehiculos):

    def __init__(self, marca_VElectrico, modelo_VElectrico):

        super().__init__(marca_VElectrico, modelo_VElectrico)

        self.autonomia = 80

    def cargaElectrica(self):

        self.cargando = True

# * HERENCIA MULTIPLE *
# * nO ESTAN PERMITIDAS O NO ES ACONSEJABLE HACER MULTIPLES HERENCIAS
# * python nos permit hacer esto, en cambio otros lenguajes tenemos que albergar
# * todas las superclases en una.
# * Curiosidad con los constructores: Que pasa si estas superclases tienen sus constructores?
# * Cual constructor va heredar la subclase?. El constructor que va heredar sera el primero
# * que colocamos en los () al momento de crear la subclase.


class biciElectrica(VELectricidad, vehiculos):

    def estado(self):

        super().estado()
    

# ***********************************************************


# * Moto

miMoto = Moto('Susuki', 'TR-45')

miMoto.estado()

print('*' * 50)

miFurgo = Furgoneta('Renault', 'Kangoo')

miFurgo.arrancar()

miFurgo.estado()

# * Bici electrica

print('*' * 50)

biciElec = biciElectrica('tesla', 'm800')

biciElec.arrancar()

biciElec.estado()

biciElec.cargaElectrica()
