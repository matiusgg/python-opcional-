from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import CSRFProtect
from cambioImg.CambioImg import CambioImg

app = Flask(__name__)
# app.secret_key = 'examen_final'
# csrf = CSRFProtect(app)

#* Objeto
cambioObjt = CambioImg()

#* Ruta
@app.route('/')
def redireccionar():

    return redirect('/home')

@app.route('/home')
def home():

    global cambio

    cambio = 'primer'

    return render_template('home.html', cambio=cambio)


@app.route('/home', methods=['POST'])
def homeLlegada():

    cambio = 'segundo'

    inputCambio = request.form['inputCambiar']

    randomMontain = cambioObjt.random(inputCambio)

    return render_template('home.html', random=randomMontain, cambio=cambio)



@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)