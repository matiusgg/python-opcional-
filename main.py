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

    # email = request.form['email']
    # password = request.form['password']

    # print(email, password)

    if request.method == 'POST':

        try:
            email = request.form['email']
            password = request.form['password']

            #* 1 Comprobar en mysql si existe ese email
            bd = Bd('localhost', 'usuario', 'mysql', 'logear')
            #* #* Comprobar en mysql si existe el email
            leer_email = bd.query(
                f'SELECT email from usuarios WHERE email="{email}"'
            )

            print(leer_email)

            if leer_email != ():

                # * Segunda comprbacion si la primera esta bien
                # *Comprobacion de email y password en la misma tupla.
                bd_total = Bd('localhost', 'usuario', 'mysql', 'logear')
                leer_email_password = bd_total.query(
                f'SELECT email, contrasenya, usuario FROM usuarios WHERE email="{email}"'
                )

                print(leer_email_password)
                
                bd = Bd('localhost', 'usuario', 'mysql', 'logear')
                #* Comprobar en mysql si existe la constraseña
                leer_password = bd.query(
                f'SELECT contrasenya from usuarios WHERE contrasenya="{password}"')

                print(leer_password)

                #* Si el email y la contraseña de la BD son igual al email y contraseña de los inputs. Redireccioname a dentro.html
                if leer_email_password[0][0] == email and leer_email_password[0][1] == password:
                    #* iniciar sesion 
                    #* Limpiamos la session cada vez que haga una nueva session.
                    session.clear()
                    session['usuario'] = leer_email_password[0][2]
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

        usuario = session['usuario']
        email = session['email']
        password = session['password']

    else:
        usuario = ''
        email = ''
        password = ''

    # return f'Datos: {email} y {password}'


    return render_template('dentro.html', email=email, password=password, usuario=usuario)
    
#******************************************
@app.route('/registro')
def registro():

    return render_template('registro.html')

#******************************************
@app.route('/registro', methods=['GET', 'POST'])
def datosRegistro():

    if request.method == 'POST':

        try:

            usuario = request.form['usuario']
            email = request.form['email']
            password = request.form['password']

            #* 1 Comprobar en mysql si existe ese email
            bd = Bd('localhost', 'usuario', 'mysql', 'logear')
            #* #* Comprobar en mysql si existe el email
            insertarTupla = bd.query(
                f'INSERT INTO usuarios (usuario, contrasenya, activo, email) VALUES("{usuario}", "{password}", 1, "{email}");'
            )

            return redirect(url_for('home'))

        except IndexError:
            
            return render_template('registro.html', no_registro=True)


    return render_template('registro.html')


#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)