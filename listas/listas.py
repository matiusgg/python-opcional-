'''
LISTAS
Parecidas a los arreglos(arryas)
'''
# Podemos poner booleanos, enteros, floats, incluso una lista dentro de una lista

grupo = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 23, True]

# si ponemos click derecho python interactive window para ver las variables y su contenido

# Multiplica relemntos de una lista, es decir, el contenido de esa lista

grupo = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 23, True]*4

print(grupo, '\n')

# Imorimir elemntos de una lista

# Imprmir elemntos seleccionados de una lista.
# IMPORTANTE: Las posiciones de los elementos de una lista son igual que en una array, es decir, 0,1,2,3,4,5,etc.
# TIP: Si solo queremos sacar una cierta los elementos desde una posicion a otra posicion de la lista
# Usamos ":", EJM: 2:5. El elemento de la posicion 2 al 5

print(grupo[2:5])

# Agregar elementos al final de una lista
# APPEND(): nos permite agregar un elemnto al final de una lista

grupo.append('Final')
print(grupo, '\n')

# Agregar elementos entre la lista
# INSERT(): Nos permite insertar en cualquier parte de la lista un nuevo elemento
# Especificamos la posicion la cual queremos que este est6e nuevo elemnto
grupo.insert(2, 'centro')
print(grupo, '\n')

# Varios elementos en una lista al final de esta
# EXTEND(): Permite agregar varios elemtnos a una lista, en donde mediante [colocamos los nuevos emtodos que queremos introducir]

grupo.extend(['Hola', 'patata', 20, 100])

print(grupo, '\n')

# Podemos concatenar listas como en los arrays, es decir con "+"
# ES

otroGrupo = ['La tierra', 'La luna', 'Jupiter']

grupofinal = grupo + otroGrupo

print(grupofinal, '\n')

# Saber si un elemnto o valor esta dentor de una lista
# in: Permite elaborar una condicion o pregunta en donde con este nos indica si ese valor o elemtno esta dentor de la lista en este caso


print(30 in grupofinal)

# SAber en que posicion de la lista se encuentra el elemento
# INDEX(): nos permite saber la posicion de un elemnto de una lista

print(grupofinal.index('centro'))

# Contar cuantas veces se repite un elemento o valor en una lista
# COUNT(): Nos permite contar cuantas veces re repite el mismo elemnto

print(grupofinal.count('Lunes'))

# Eliminar el ultimo elemnto de la lista
# POP(): Nos permite eliminar elemntos de una lista, si no leintroducimos nada en (). Eliminara el ultimo
grupofinal.pop()
print(grupofinal, '\h')


# Eliminar un elemento de una lista
grupofinal.pop(5)
print(grupofinal, '\h')

# Eliminar el elemnto exacto de una lista
# REMOVE(): Nos permite eleiminar elemtnos de una list,, es decir, da igual la posicion, tenemos que especificar el valor del elemento

grupofinal.remove('Lunes')
# Voltear una lista, es decir ponerla alreves
# REVERSE(): Nos permite voltear o poner al revez una lista, por lo cual las posiciones se cambiar, el ultimo seria el primero y el primero el ultimo por ejemplo

grupofinal.reverse()

# Si queremos ordenar una lista
# SORT: Solo nos permite ordenar una lista, no una concatenacion de listas
grupofinal.sort() # descendente
grupofinal.sort(reverse=True) # Ascendente: mayor a menor si son enteros

# Borrar todo el contenido de la lista
# CLEAR(): Nos permite borrar los elementops de una lista
grupofinal.clear()

# Si queremos cambiar un elemento de la lista.
# Especificamos la posicion con [] y con "=" le damos el nuevo valor a ese elemento
grupofinal[5] = 'Otra cosa'

'''
TUPLAS: Sirven concretamente para buscar, consuymen menos memoria de las listas
Son mas rapidas, pero despue sde crearlas son inmodificables

'''
# Ya no empleamos [] sino ().
tupla01 = ('Lunes', 'Martes', 'Miercoles')

print(tupla01, '\n')

# Nos de la longitud de esta tuple
# LEN: Nos permite sacar la longitud de una tupla o lista

print(len(tupla01), '\n')

# Saber si un valor esta dentor de una tupla

print('Martes' in tupla01)

# Saber en que poscion esta un elemento de la tupla

print(tupla01.index('Miercoles'))

# Contar cuantas vece se repite un elemtno en una tupla

print(tupla01.count('Miercoles'))

# Copiar el contenido de una tupla a una lista
# No lo estamos moviendo estamos copiando
# Esto nos beneficia porque las tuplas son inalterables y al usar LIST(), esta tupla se vuelve lista automaticamente,
# y asi pòder modificarla con las opciones que tenemos con una lista

nuevaLista = list(tupla01)

# Si al contrario queremos copiar el cnotenido de una lista a una tupla, esto con TUPLE()

nuevaTupla = tuple(grupofinal)