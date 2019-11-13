#* IMPORTANTE: cADA VEZ QUE HAGAS UNA QUERY HAY CREAR UN NUEVO OBJETO
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

    return redirect(url_for('homeSesion'))

#******************************************

#******************************************
@app.route('/home', methods=['GET', 'POST'])
def homeSesion():

    #* Simplemente con un FORM en dentro.html que dentro de este hay un boton para volver a home.html.
    #* Podemos decirle que nos borre las sessiones que tengamos.
    #* IMPORTANTE: Si estamos en navegador Privado/incognito no nos borrara la COOKIE.
    if request.method == 'POST':

        session.clear()
    
    #* Si no es mediante el boton VOLVER de dentro.html y la persona escribe en la URL /home. Este condicional
    #* Lo que hara es volver a login si hay una session abierta. Esto para evitar que la persona este navegando
    #* en la app mediante las URLS sin ninguna session o permiso.
    if 'email' in session:

        return redirect(url_for('login'))

    
    return render_template('home.html')

#******************************************
@app.route('/login')
def login():

    return render_template('login.html')

#******************************************
@app.route('/login', methods=['GET', 'POST'])
def datos():

    # email = request.form['email']
    # password = request.form['password']

    # print(email, password)

    if request.method == 'POST':

        try:
            email = request.form['email']
            password = request.form['password']

            #* IMPORTANTE: cADA VEZ QUE HAGAS UNA QUERY HAY CREAR UN NUEVO OBJETO
            bd = Bd('localhost', 'usuario', 'mysql', 'logear')
            #* #* Comprobar en mysql si existe el email
            leer_email = bd.query(
                f'SELECT email from usuarios WHERE email="{email}"'
            )

            print(leer_email)

            #* Si en la BD no esta vacio, entonces el email que se ingreso en el input existe en la BD
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
                #* No necesita estar en un codicional, ya el condicional te lo hace el WHERE
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
                    return render_template('login.html', no_usuario=True)
            else:
                return render_template('login.html', no_usuario=True)

        #* IndexError nos permite manejar el error cuando el email no esta en la base de datos.
        except IndexError:

            return 'No existe el email en la base de datos'

    return render_template('login.html')

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

        usuario = request.form['usuario']
        email = request.form['email']
        password = request.form['password']

        
        bd = Bd('localhost', 'usuario', 'mysql', 'logear')

        leer_email = bd.query(
                f'SELECT email from usuarios WHERE email="{email}"'
        )


        print(leer_email)

        #* Si leer_email tiene elementos significa que el input que se introdujo en registrar.html esta en la BD,
        #* por lo tanto obviamente no puede registrarse con el mismo email, si pasa esto mandame email_existe.
        if leer_email != ():

            return render_template('registro.html', email_existe=True)

        bd2 = Bd('localhost', 'usuario', 'mysql', 'logear')
        #* Insertar tupla
        insertarTupla = bd2.query(f'INSERT INTO usuarios (usuario, contrasenya, activo, email) VALUES("{usuario}", "{password}", 1, "{email}");')

        print(insertarTupla)
        return redirect(url_for('login'))

        #*****************************************************************

    return render_template('registro.html')

#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)