from flask import Flask, url_for, session, request, redirect, render_template
from ahorcado.Ahorcado import Ahorcado
import random
import csv

#* Inicializar nuestra clase de conexion a la BD


#* Intanciar Flask
app = Flask(__name__)

#* Crear un llave/clave secreta para SESSION
app.config['SECRET_KEY'] = 'SUPER SECRETO'

#* Crear rutas
#* En donde verficaremos si en mysql existe ese usuario.
#* Si no, enviar como alternativa al usuario a volver a intentar o a registrarse.
#* Si es registro, crear la SESSIOn con los datos del usuario.
#******************************************
@app.route('/')
def redireccionar():

    return redirect(url_for('home'))

#******************************************
@app.route('/home')
def home():



    return render_template('home.html')

#******************************************
@app.route('/ahorcado')
def ahorcado():


    
    return render_template('ahorcado.html')

#******************************************

palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']
nuevoRandom = random.choice(palabras)

listaImagenes = ['inicio', 'cabeza', 'torso', 'brazoderecho', 'brazoizquierdo', 'piernaderecha', 'pierdes']

@app.route('/ahorcado', methods=['POST'])
def ahorcadoDatos():

    # palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

    # palabraRandom = random.choice(palabras)

    letraInput = request.form['letra']
    
    activar = request.form['activar']
    

    # objLetra = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
    objLetra = Ahorcado()

    #*Palabras ocultas
    ocultas = ''

    playAhorcadito = objLetra.ahorcadito(letraInput, activar, nuevoRandom)

    print(f'Play Ahorcadito: {playAhorcadito}')

    for img in listaImagenes:

        if playAhorcadito == img:

            str(img)
        else:
            print('play no es igual a la lista de imagenes')

    #***********************

    return render_template('ahorcado.html', random=nuevoRandom, play=playAhorcadito, nombreImagen=img)

#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)

