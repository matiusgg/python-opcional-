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

i = 0

for llave, valor in ofertas.items():

    columna = '''<div class="''' + llave + '''">

    <div class="logo"> <img src="{{ url_for('static', filename='img/''' + valor['img'] + ''') }}" alt="logo1"> </div>

        <div class='titulo'> <h1>  {{ ''' + valor['titulo'] + ''' }} </h1> </div>
        <div class='descripcion'> <h3> {{''' + valor['descripcion'] + ''' }}</h3> </div>
        <div class='precio'> <h1> {{ c''' + valor['precio'] + ''' }} </h1> </div>
        <div class='link'> <h3> {{ ''' + valor['link'] + ''' }} </h3> </div>
        <div class='boton'> <button type="submit"> {{ ''' + valor['boton'] + ''' }} </button> </div>
    
    </div>'''

    print(columna)

   