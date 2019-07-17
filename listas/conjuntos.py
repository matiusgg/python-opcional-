'''
CONJUNTOS: EN LOS CONJUNTOS no se pueden repetir los datos, porque basicamente
no los alamacwna auqneu le forcemos. Tampoco no se pueden meter dentro de conjuntos ni listas, ni tuplas
ni otros conjuntos.

Los conjuntos son grupos de datos desordenados
'''

# SET(): Si ponemos conjutno igual a llaves, se preguntara si se creara una tupla o lista y 
# Solo cuando creemos conjuntos vacios de incio para despues introducirle elementos, por eso encesitamos el SET() para que sepa que es un CONJUNTO no una
# lista o una tupla, es decir con solo ponerle SET() una vez, todo lo que viene despues al momento de poner crear conjuntos con {}, lo interpretara como elemtnos del conjunto

conjuntos01 = set()
conjuntos01 = {}

# Crear conjunto
conjuntos01 = {'Lunes'}


# Agregar nuevos elementos. Que se van a insertar en lugares aleatorios(pero no random, ya si cargamos
# el terminal de nuevo seguira en esa posicion solo sera aleatorio una vez que se introduzca y asi se quedara)
# ADD(): Nos hace lo explicado anteorioremente

conjuntos01.add('Nuevo Dia')

print(conjuntos01)

# Eliminar un elemnto o valor del conjunto
# DISCARD(): Nos permite eliminar un elemtno o valor de un conjunto sin qtener que especificarle la posicion, es ya lo sabra

conjuntos01.discard('Lunes')

print(conjuntos01, '\n')


# Buscar elementos dentro de un conjunto
# IN: ya lo usamos en tuplas y listas
# NOT IN: Verifica si un elemtno no esta en un conjunto/lista/tupla. Si no esta nos pondra TRUE obviamente

print(2 in conjuntos01)

# Comprobar si ambos conjuntos son iguales
# se recuerda al SQL con los JOINs
# Simplemente con "==" podemos indicarle si son iguales, si los son te pone TRUE sino FLASE

conjuntos02 = {1,2,3}
conjuntos03 = {3,1,2}

print(conjuntos02 == conjuntos03)

# Union de dos conjuntos
# con "|" podemos unir conjuntos.
# Pero al momento de unirlos, si encuentra en la union algun elemtnos repetido en ambos, no colocara
# ambos elemtnos sino que solo pondra una vez ese elemento, ya que como se dijo, los conjuntos no tienen elementos repetidos
union = conjuntos02 | conjuntos03

print(union)

# En la Intercepcion de dos conjuntos. Los elementos que se repiten los queremos separar
# Es decir, nos va averiguar cuale sson los elemtnos que se estan repitirendo y nos mostrara
# con print ese elemento que se repite en ambos, aqui no se une ni nada solo nos averigua esa peticion que le dimos con "&"

intersepcion = conjuntos02 & conjuntos03

print(intersepcion)

# Mostrar cuales elementos son diferentes entre conjuntos.
# Podemos indicarle que nos muestre con PRINT que elemtnos de un conjutno no tiene otro
# elemtnos del conjunto03 que no tiene el conjunto03

diferencia = conjuntos02 - conjuntos03

print(diferencia)

# La difernecia Simetrica. Elemtnos que etsan en A y B, pero no en ambos.
# Es decir, dame los elemtnos que no se repite en ambos conjuntos

simetrica = conjuntos02 ^ conjuntos03

print(simetrica, '\n')

# Saber si es un subconjunto
# SUBCONJUNTO: Si los elemtnos de ese conjunto estan tambioen dentro del conjunto "padre"
# isseubset(): NOs permite colocar si un conjunot es subcojunto de otro. Lo que hace basicamente
# es verificar o comparar si embos conjunntos tienen los mismos elemtnos en ambos del subcojunto
# cojnuto02 = {1,2,3}. Cmo vemos conjunto02 si conjunto04 comparten 1,2,3 por lo cual conjunto04 es subconjunto

conjuntos04 = {1,2,3,4,5}

print(conjuntos02.issubset(conjuntos04))

# SAber si un conjunto es un superconjunto
# Para ser un superconjunto ambos conjunto deben tene rlos mismos elemtnos
# conjuntos01 = {1,2,3,4,5}
# conjuntos04 = {1,2,3,4,5}

print(conjuntos02.issuperset(conjuntos04))

# SAber si son disconexos. No tiene que compartir ningun elemento

print(conjuntos02.isdisjoint(conjuntos04))

# como hacer que un conjunto sea inmutable
# frozenset(): Lo que hace es poner el conjunto inmutable, como en una tupla

conjuntos04 = {3,6,8,100}

conjuntos04 = frozenset({3,6,8,100})

# Borrar todo el contenido

conjuntos01.clear()

