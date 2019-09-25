
# * HACER DIRAGRAMA DE FLUJO
# * fUNCIONE EN CONSOLA
# * WEB
# * 1900-2020

# horoscopo = {
#     'rata': [1900, 1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2016],
#     'Buey': [1901, 1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2017],
#     'Tigre': [1902, 1914, ],
#     'Conejo': [1903],
#     'Dragon': [1904],
#     'Serpiente': [1905],
#     'Caballo': [1906],
#     'Oveja': [1907]
#     'Mono': [1908],
#     'Gallo': [1909],
#     'Perro': [1910],
#     'Cerdo': [1911]
# }

# horoscopo = {
#     'rata': [],
#     'Buey': [],
#     'Tigre': [],
#     'Conejo': [],
#     'Dragon': [],
#     'Serpiente': [],
#     'Caballo': [],
#     'Oveja': [],
#     'Mono': [],
#     'Gallo': [],
#     'Perro': [],
#     'Cerdo': []
# }


# for animal, anyos in horoscopo.items():

#     anyoInicio = int(input('Anyo: '))

#     anyos.append(anyoInicio)
    
#     while anyoInicio < 2030 and animal == 'rata':

#         anyoInicio += 12

#         anyos.append(anyoInicio)

#         print(anyoInicio)

#         print(anyos)

# * Forma profesor



animales = ['mono', 'gallo', 'perro', 'cerdo', 'rata', 'buey', 'tigre', 'conejo', 'dragon', 'serpiente', 'caballo', 'cabra']

def run(usuario):

    for i in range(0,12):

        if usuario % 12 == i:

            print(i)

            print(animales[i])

def tuHoroscopo():

    try:
        global usuario
        usuario = int(input('Introduce el año: '))
        run(usuario)

    except ValueError:

        print('Introducec un año exacto, no una fecha')
        tuHoroscopo()


if __name__ == "__main__":
    
    tuHoroscopo()

            

