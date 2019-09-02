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
# Usamos ":", EJM: 2:5. El elemento de la posicion 2 al 5. pero el 5 no te lo muestra solo el penultimo

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


# Eliminar un elemento de una lista mediante la posicion/index
grupofinal.pop(5)
print(grupofinal, '\h')

# Eliminar el elemnto exacto de una lista
# REMOVE(): Nos permite eleiminar elemtnos de una list,, es decir, da igual la posicion, tenemos que especificar el valor del elemento

grupofinal.remove('Lunes')
# Voltear una lista, es decir ponerla alreves
# REVERSE(): Nos permite voltear o poner al revez una lista, por lo cual las posiciones se cambiar, el ultimo seria el primero y el primero el ultimo por ejemplo

grupofinal.reverse()

# Si queremos ordenar una lista
# SORT: Solo nos permite ordenar una lista, no una concatenacion de listas. Nos beneficia si queremos ordenar enteros de menor a mayor o viceversa.
grupofinal.sort() # descendente
grupofinal.sort(reverse=True) # Ascendente: mayor a menor si son enteros

# Borrar todo el contenido de la lista
# CLEAR(): Nos permite borrar los elementops de una lista
grupofinal.clear()

# Si queremos cambiar un elemento de la lista.
# Especificamos la posicion con [] y con "=" le damos el nuevo valor a ese elemento
grupofinal[5] = 'Otra cosa'

# Poner la priumera letra en mayuscula

grupofinal.capitalize()

# poner todo en minusculas

grupofinal.lower()

# poner todo en Mayusculas

grupofinal.upper()

# lo que esta en mayuscula te lo pone en minuscula y lo que esta en minuscula te lo pone en mayusculas

grupofinal.swapcase()

# Poner la primera letra de cada palabra en mayuscula

grupofinal.title()

# Nos permite centrar los elementos y poner caracteres alrededor, donde (CEntrar los elementos, caracteres que queremos que este alrededor)

grupofinal.center(50, '*')

# Nos permtie poner los elemtnos al final de la sentencia y poner caracteres antes de estos. r->right

grupofinal.rjust(50, '*')

# Nos permtie poner los elemtnos al principio de la sentencia y poner caracteres despues de estos. l-left

grupofinal.ljust(50, '*')

# ZFILL: Si tenemos un numero, esto nos permite rellenar con ceros la cantidad que le pongamos a la izquierda.

grupofinal.zfill(10)

# FIND: NOs permite averiguar en que posicion esta un elemento, nos dira la posicion con numero, aunque seas un STRING y le pongamos "mañana por ejemplo"
# Nos dira

grupofinal.find('mañana')

# unir Strings o valores de una coleeccion con el caracter que le indiquemos en '' y en (le indicamos la lista).

print(' '.join(equipoNBA))

# SPLIT(): Nos permite separa palabras de una cadena de STRING, en donde (ponemos el caracter que nos permititra sepaarar por cada palabra)

print(equipoNBA.split('_'))

# REPLACE(): Nos permite reemplzar/sustituir un elemento por otro, nos ayuda si tenemos un STRING.

equipoNBA.replace('h', 'hh')

#ENUMERATE: Nos permite recoger los datos o valores de la posicion que ocupa ese valor o dato

enumerate(self.contactos)

# DEL: BOrrar el valor de una lista

del contactos[index]






'''
TUPLAS: Sirven concretamente para buscar, consuymen menos memoria de las listas
Son mas rapidas, pero despue sde crearlas son inmodificables

'''




# Ya no empleamos [] sino ().
tupla01 = ('Lunes', 'Martes', 'Miercoles')

print(tupla01, '\n')

# Nos de la longitud de esta tuple
# LEN: Nos permite sacar la longitud de una tupla o lista
# si lo usamos en un bucle tenemos que indicar con -1 porque el LEN nos da la longitud incluyendo boviamente el valorc de la posicion 0.
# 

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

# SILCE: DREBANAAS/ Nos permite cortar o separar elementos. en donde en los [posicion en la cual queremos partir:(opcional)posicion hasta donde queremos partir]



texto = 'Hola'

texto[1:] # ola

texto[1:3] # ola

# Con lo mismo que en RANGE, el 3 digito nos permite definir cuantos saltos queremos hacer entre los elementos

texto[1:4:]

# Para poner al revez un string
texto[::-1]




