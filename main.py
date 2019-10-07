from flask import Flask, request, make_response, redirect, render_template, session, url_for
from signo.signo import HoroscopoChino


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SUPER SECRETO'


@app.route('/')
def redireccionar():

    return redirect('/home')


@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/home', methods=['POST'])
def llegada():

    # REquest.FOrm: Alberga los datos del <FORM>
    anyo = int(request.form['anyo'])

    global signo_usuario
    global descripcion_signo
    global compatibilidad
    # Creando un objeto
    persona = HoroscopoChino(anyo)

    # Llamamos al metodo que tiene el objeto de la clase

    signo_usuario = persona.signo()

    descripcion_signo = persona.descripcion()

    compatibilidad = persona.compatibilidad()

    return redirect(url_for('signo'))


@app.route('/signo', methods=['GET'])
def signo():

    return render_template('signo.html', signo_usuario=signo_usuario, descripcion=descripcion_signo, compatibilidad1=compatibilidad[0], compatibilidad2=compatibilidad[1])


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
