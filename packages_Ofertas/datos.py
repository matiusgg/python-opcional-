
# ofertas = {}


# def ofertas():

#     i = 0

#     while i < 3:

#     titulo = input('Introduce el titulo de la oferta')

#     i += 1

ofertas = {

    'columna1': {

        'img': 'logo1.png',
        'titulo': 'Core',
        'descripcion': 'everythin',
        'precio': '5',
        'link': 'All core features',
        'boton': 'Included',
    },

    'columna2': {

        'img': 'logo2.png',
        'titulo': 'Adapt',
        'descripcion': 'customize',
        'precio': 'free',
        'link': 'arrows',
        'boton': 'Included',
    },

    'columna3': {

        'img': 'logo3.png',
        'titulo': 'Localize',
        'descripcion': 'Add',
        'precio': '10',
        'link': 'languages',
        'boton': 'Included',
    },


}

print(ofertas['columna1']['titulo'])
