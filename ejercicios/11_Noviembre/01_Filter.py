'''

Filtrar datos de Jugadores de Basket

'''

#* Hacer una clase para recoger los datos de jugadores(nombre, posicion, puntosXpartido)


class Jugadores():

    def __init__(self, nombre, posicion, puntosXpartido):

        self.nombre = nombre
        self.posicion = posicion
        self.puntosXpartido = puntosXpartido

    #* FUNCION STRING: Nos permite devolver un String como el ToString() de JAVA.
    #* No es un metodo, es como un constructor pero para que nos devuelva los atributos en un formato string.
    def __str__(self):

        return f'nombre Jugador: {self.nombre}, Su posición es: {self.posicion} y su Score es: {self.puntosXpartido}'

        

jugadorObjt = Jugadores('michael', 'pivote', 20)
print(jugadorObjt)

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

#*Hacemos el FILTER, en donde filtramos los jugadores que tengan mas de 10 puntos por Partido.
#* en el parametro punto10 ira cada objeto de la lista, por lo cual al poner punto10.atributo
#* no nos debería dar problema por simplemente estamos llamando al atributo del objeto.
filterJugadores = filter(lambda punto10: punto10.puntosXpartido >= 10, jugadoresDelEquipo)
#* Si usamos el PEP 8 y tenemos una linea con codigo muy largo, el pepe8 lo pondra hacia abajo pero en la misma linea.

#* Si vemos que un LIST() o TUPLE() no funciona y nos sale el codigo del OBJECT, usamos un bucle FOR

for jugadorScore in filterJugadores:
    #* Nos devolvera el ToString()
    print(jugadorScore)