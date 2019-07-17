'''
DiCCIONARIOS: Los Elementos tambien son desordenados, pero a difernecia de los conjuntos
no usamos el SET() y se utliza la LLAVE - VALOr

'''

# Diccionario vacio, para inicaR LA VARIABLE
# Usamos {}

diccionario = {}

# diccionario

diccionario = {

    'rojo': 'red',
    'lapiz' : 'pencil'
}

print(diccionario)

# Sacar el valor de una llave: Usamos "[]" para poner el nombre de llave, y asi que nos de el valor de esa llave

print(diccionario['rojo'], '\n')



# Agregar nuevos elemtnos al diccionario
# en "[]" ponemos el nombre de la llave y con "=" ponemos el valor para esa llave
diccionario['perro'] = 'log'

# Modificar un elemento de un diccionario, ponemos el nombre de la lñave y le asignamos el nuevo valor

diccionario['rojo'] = 'REDingles'

# Eliminar un elemento
# DEL(): Nos permit borrar un elemento, como vemos especificamos con "[]" la llave, para saber cual elemtno borrar


del(diccionario['rojo'])

# Poner listas dentro de diccionarios, en este la lista la ponemos en el valor de la LLAVE

agenda01 = {

    'Pepe': [23,1.72],
    'Maria': [24,1.80],
    'Pedro': [32, 1.70]
}

print(agenda01['Maria'])

# Diccionario dentro de otro Diccionario

agenda02 = {

    'Pepe': {'edad':33, 'altura':1.7},
    'Maria': {'edad':22, 'altura':1.8},
    'Juan': {'edad':44, 'altura':1.9},
    'Eva': {'edad':66, 'altura':2.0},
}

print(agenda02)

print(agenda02['Maria'])

# *************************************************************************************************

# equipo NBA

equipoNBA = {

    23:'Michael Jordan',
    00:'Robert Parish',
    21:'Dominique Wilkins',
    33:'Larry Bird',
    24:'Dennid Rodman',
    34:'shquile 0\'neal',
    24:'Moses Malone'
}

# Sacar el valor, sabiendo que existe la llave

print(equipoNBA[00])

# Sino sabemos que la llave puede existir, aqui nos va ayudar la funcion GET()

# GET(): Nos permite verifica rsi una llave existe o no, lo que hace es GET(nombreDeLaLLave"Si existe te lo pone", sino exste colocame esto)
# ÇEn este caso la llave 23 existe, por lo cual nos mostrar ale valor, si pusieramos una llave que no este, nopostra lo que hay despue de la coma
print(equipoNBA.get(23, 'No existe'))

# Busqueda o peticion

print(23 in equipoNBA)

# Enseñar solo los KEYS's

print(equipoNBA.keys())

# Enseñar solo los valores

print(equipoNBA.values())

# Enseñame LLAVE-VALOR. No hacer segun cual diccionario

print(equipoNBA.items())

# Borrar diccionario

print(equipoNBA.clear())
