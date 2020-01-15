'''
FUNCIONES DE ORDEN SUPERIOR
MAP: Toma una funcion y una lista, y aplica esa fucnion a cada elemtnos de esa lista, donde produce una nueva lista.
Aqui aplicamos una función a cada elemento de una lista y a diferencia de en el FILTER en donde se aplicaba una condicion.
Esto nos da mas opciones porque ya no solo le aplicamos una condicion a los elementos de una lista, si no que tenemos más
margen de cosas que podemos ahcer al aplicarle una funcion a cada elemento. Por lo cual MAP es más potente.
'''

#* Mismo ejercicio de jugadores pero en vez de FILTER usamos MAP.
class Jugadores():

    def __init__(self, nombre, posicion, puntosXpartido):

        self.nombre = nombre
        self.posicion = posicion
        self.puntosXpartido = puntosXpartido

    #* FUNCION STRING: Nos permite devolver un String como el ToString() de JAVA.
    #* No es un metodo, es como un constructor pero para que nos devuelva los atributos en un formato string.
    def __str__(self):

        return f'nombre Jugador: {self.nombre}, Su posición es: {self.posicion} y su Score es: {self.puntosXpartido}'

        

jugadorObjt = Jugadores('michael', 'pivote', 0)
print(self.nombre)
jugadorObjt2 = Jugadores('BoquitaGrandexD', 'delantero', 9)
jugadorObjt3 = Jugadores('Jordan', 'defensa', 40)
jugadorObjt4 = Jugadores('MessiChiquito', 'delantero', 50)
jugadorObjt5 = Jugadores('Khabib', 'defensa', 60)

#* Ponemos las instancias de los objetos en una lista para el FILTER:
jugadoresDelEquipo = [
    jugadorObjt,
    jugadorObjt2, 
    jugadorObjt3,
    jugadorObjt4,
    jugadorObjt5
]

#* Creamos una funcion para saber que comisión por puntos se lleva cada jugador
#* Por ahora sin MAP
def calcular(puntosJugador):

    #* Como vemos no es una condicion
    # puntosJugador.puntosXpartido *= 30

    #* Solo si se supera los 10 puntos tienen comision de 30 euros.
    if puntosJugador.puntosXpartido > 10:
        
        puntosJugador.puntosXpartido *= 30
        #* Como vemos puntosJugador ya de por si lleva el __str__() por lo cual no tenemos llamarlo ni tambien
        #* ir a __str__() a  agregarle el atributo comision por que no es necesario. ya que en si el objeto
        #* trae el __str__() y simplemente agregarle la operacion de comisión.
        puntosjugador = str(puntosJugador) + f'y su comisión es {puntosJugador.puntosXpartido}€'

    elif puntosJugador.puntosXpartido == 0:

        puntosJugador = f'El jugador {str(puntosJugador.nombre)} al banquillo'
  
    puntosJugador.nombre = puntosJugador.nombre.upper()

    return puntosJugador

#* Ahora con mapping tendriamos: Lo que hara MAP() es aplicar a cada elementos de la lista una funcion.
jugadorComision = map(calcular, jugadoresDelEquipo)

#* Ahora para imprimirlo lo llevamos a un FOR
for comision in jugadorComision:

    print(comision)
