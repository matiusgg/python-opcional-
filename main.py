from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from pais.Pais import Pais


app = Flask(__name__)


@app.route('/')
def redireccionar():

    return redirect('/pais')

@app.route('/pais')
def pais():

    return render_template('pais.html')


@app.route('/pais', methods=['POST'])
def datos():

    paisInput = request.form['pais']

    global poblacion

    objetoPais = Pais(paisInput)

    poblacion = objetoPais.jsonPais('static/json/paises.json')

    return render_template('poblacion.html', poblacion=poblacion)


@app.route('/poblacion', methods=['GET'])
def signo():

    return render_template('poblacion.html', poblacion=poblacion)


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'





if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
