# * IMPORTACIONES del FLASK y del PAQUETE donde se alberga la CLASE Libreria()
from flask import Flask, request, make_response, redirect, render_template, session, url_for
from libreria.Libreria import Libreria

# *****************************************
# * variable APP
app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************

# *Ruta que direcciona a '/home'
@app.route('/')
def redireccionar():

    return redirect('/home')
    

# *****************************************

# *Ruta HOME
@app.route('/home')
def home():

    return render_template('home.html')

    # *****************************************

# # *Ruta HOME
@app.route('/home', methods=['POST'])
def llegadahome():

    libro = request.form['libro']

    libreriaObjt = Libreria(libro)

    lista = libreriaObjt.Busqueda()

    return render_template('home.html', autor=lista[0], libro=lista[1], precio=lista[2])

# *****************************************

# * RUTA PAGINA ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


# * MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)