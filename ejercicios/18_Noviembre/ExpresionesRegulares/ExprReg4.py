"""

METACARACTERES
--------------
(caracter comodin): Los METACARACTERES nos permiten condicionar la busqueda.

"""

import re
gente = [
    'Pedro Antonio',
    'Pepe Gonzalez',
    'María de Santos',
    'Cati Ripoll',
    'María Fort'
]

#* Buscar en la lista el nombre
for nombre in gente:

    #*METACARACTER(^): Nos ayudara a hacerf la busqueda al principio del String
    if re.findall('^Cati', nombre):
        #* nos devolvera todo el contenido del string si lo encuentra.
        print(nombre)

#* Buscar por apellido
for nombre in gente:

    #*METACARACTER($): Nos ayudara a hacerf la busqueda al final del String
    if re.findall('Ripoll$', nombre):
        print(nombre)

print('*' * 50)


lista = [
    'http://www.hola.com',
    'http://www.hola.es',
    'http://www.hola.it',
    'http://www.hola.fr',
    'https://www.hola.com'
]

#* Buscar en la lista URL mas segura
for url in lista:

    if re.findall('^https', url):
        print(url)

#* Buscar en la lista URL de un pais
for url in lista:

    if re.findall('fr$', url):
        print(url)

#------------- RANGOS-----------------------

print('*' * 50)

for url in lista:

    #*METACARACTER([]): Nos ayudara a buscar si hay caracteres, es decir. no buscara la palabra [áÁ]
    #* sino que buscara la á, Á por separado no com si fuera una palabra.
    if re.findall('[áÁ]', url):
        print(url)

gente = [
    'Pedro',
    'Pepe',
    'María',
    'Catí',
    'María'
    ]

#* buscar en la lista un rango entre ...
for nombre in gente:

    #* Estamos buscando entre la a y la b. El '-' nos sirve para indicarle si el string tiene las letras entre una y otra.
    #* Es decir, en un string buscar si este string tiene caracteres entre h y z
    if re.findall('[h-z]', nombre):

        print(nombre)

print('*' * 50)

#* buscar en la lista un rango entre ...
for nombre in gente:

    #* IMPORTANTE: No podemos poner en los [letra1-letra2] la mezcla entre minuscula y mayuscula debem ser ambas minusculas
    #* o ambas mayusculas
    if re.findall('^[A-C]', nombre):

        print(nombre)

print('*' * 50)

#* buscar en la lista un rango entre ...
for nombre in gente:

    if re.findall('[o-y]$', nombre):

        print(nombre)

print('*' * 50)

#* Supongamos que en una BD tenemos un atributo de COdigo de ventas, donde nos informara de cuantas ventas tenemos
codigoVentas = [
    'inf1',
    'dep1',
    'inf2',
    'hogar1',
    'inf3',
    'infA',
    'infB'
]

# Buscar un codigo dentro de un rango de codigos en la session de informatica:
for codigo in codigoVentas:

    #* Como vemos estamos conbinando INF con rango, que nos permitira hacer la busqueda de aquellos
    #* INF que tiene varios numero dentro de un rango de [0-9]
    if re.findall('inf[0-9]', codigo):

        print(codigo)

#* Buscar en la lista un rango que NIEGUe su condicion
for codigo in codigoVentas:

    #* Si usamos '^' dentro de un RANGO significa una negacion, es decir, que no me hagas ese rango
    if re.findall('inf[^0-2]', codigo):

        print(codigo)

#* Buscar en la lista VARIOS RANGOS
for codigo in codigoVentas:

    #* Como vemos no neceitamos poner comas entres los rango que queremos si no que despues de uno empieza otro directamente.
    if re.findall('inf[0-3A-B]', codigo):
    #* Otro ejemplo
    # if re.findall('inf[0-9A-Za-z]', codigo):

        print(codigo)