from flask import Flask, url_for, session, request, redirect, render_template
from login.Conexion import Bd

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
@app.route('/home', methods=['GET', 'POST'])
def datos():

    if request.method == 'POST':

        try:
            email = request.form['email']
            password = request.form['password']

            #* 1 Comprobar en mysql si existe ese email
            bd = Bd('localhost', 'usuario', 'mysql', 'logear')
            #* #* Comprobar en mysql si existe el email
            leer_email = bd.query(
                f'SELECT email from logear WHERE email="{email}"'
            )

            if leer_email != ():

                #* Segunda comprbacion si la primera esta bien
                #*Comprobacion de email y password en la misma tupla.
                bd_total = Bd('localhost', 'usuario', 'mysql', 'logear')
                leer_email_password = bd_total.query(
                f'SELECT email, contrasenya FROM logear WHERE email="{email}"'
                )
                
                # bd = Bd('localhost', 'usuario', 'mysql', 'logear')
                # #* Comprobar en mysql si existe la constraseña
                # leer_password = bd.query(
                # f'SELECT contrasenya from logear WHERE contrasenya="{password}"')

                if leer_email_password[0][0] == email and leer_email_password[0][1] == password:
                    #* iniciar sesion 
                    #* Limpiamos la session cada vez que haga una nueva session.
                    session.clear()
                    session['email'] = email
                    session['password'] = password

                    return redirect(url_for('dentro'))

                else:
                    return render_template('home.html', no_usuario=True)
            else:
                return render_template('home.html', no_usuario=True)

        #* IndexError nos permite manejar el error cuando el email no esta en la base de datos.
        except IndexError:

            return 'No existe el email en la base de datos'

    return render_template('home.html')

#******************************************
@app.route('/dentro', methods=['GET'])
def dentro():
    if 'email' in session and 'password' in session:

        email = session['email']
        password = session['password']

    else:
        email = ''
        password = ''

    return f'Datos: {email} y {password}'


    # return render_template('dentro.html', email=email)
    
#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)