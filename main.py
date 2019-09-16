from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/')
def home():

    return render_template('home.html', **ofertas)


@app.errorhandler(404)
def page_no_found(error):

    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    # Esto es para que cuando vayas a un localhost, tengamos esa ruta/url con
    # lo que le pusimos en app.run('0.0.0.0', '5000'). la idea es que FLASK
    # refleje PYTHON en un navegador
    # DEBUGEADOR para que que nos saque los fallos de bug
    app.run('0.0.0.0', '4000', debug=True)
