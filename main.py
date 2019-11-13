from flask import Flask, url_for, session, request, redirect, render_template
from ahorcado.Ahorcado import Ahorcado

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

    SPRITES = [
'''
     ---
     |   |
     0   |
         |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /    |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|   |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
         |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
     |   |
         |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
     |   |
    /    |
         ---------
         ''',
'''
     ---
     |   |
     0   |
    /|\  |
     |   |
    / \  |
         ---------
         '''
]

    return render_template('home.html', sprites=SPRITES)


#******************************************
@app.route('/home', methods=['POST'])
def homeUsuario():

    usuarioInput = request.form['usuario']

    #****************************************

    objUsuario = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')

    insertarUsuario = objUsuario.query(f'INSERT INTO usuarios (usuario, contrasenya, activo) VALUES("{usuarioInput}", "123", 1);')

    #****************************************

    objUsu = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')

    comprobarUsuario = objUsu.query(f'SELECT usuario FROM usuarios WHERE usuario="{usuarioInput}";')

    if comprobarUsuario != ():

        return redirect(url_for('ahorcado'))

    return render_template('home.html')

#******************************************
@app.route('/ahorcado')
def ahorcado():


    return render_template('ahorcado.html')

#******************************************
@app.route('/ahorcado', methods=['POST'])
def ahorcadoDatos():

    letraInput = request.form['letra']

    objLetra = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')

    playAhorcadito = objLetra.ahorcadito(letraInput)

    return render_template('ahorcado.html')

#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)