from flask import Flask, url_for, session, request, redirect, render_template
from ahorcado.Ahorcado import Ahorcado
import random
import csv
#*Importar MONGO DB
from pymongo import MongoClient


#* Inicializar nuestra clase de conexion a la BD


#* Intanciar Flask
app = Flask(__name__)

#* Crear un llave/clave secreta para SESSION
app.config['SECRET_KEY'] = 'SUPER SECRETO'

#**************************************
#* ULR Conexion
MONGO_URL_ATLAS = 'mongodb+srv://mongodb:mongodb@cluster0-yxtud.mongodb.net/test?retryWrites=true&w=majority'

#* Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

#* Creacion base de datos
db = client['ahorcadito']

#* Creacion coleccion
collectionPalabra = db['palabras']

#* Crear varios documentos
# lista_Documentos = [
#     {
#         "palabra": "lampara",
#         "tipo": "objetos"
#     },
#     {
#         "palabra": "cama",
#         "tipo": "objetos"
#     },
#     {
#         "palabra": "rio",
#         "tipo": "naturaleza"
#     }
# ]

# #*INSERTMANY: nos permite insertar varios documentos
# collection.insert_many(lista_Documentos)

#* Leer todos los documentos de la coleccion
# resultados = collection.find()
# #* Lo convertimos en una lista porque sino nos lo lanza como un objeto al ser un documento
# for i in resultados:
#     print('ñ'*50)
#     print(i['palabra'])


#**************************************

#******************************************
@app.route('/palabras')
def palabras():

    return render_template('palabras.html')

#******************************************

#******************************************
@app.route('/palabras', methods=['GET', 'POST'])
def nuevaPalabra():

    nuevaPalabra = request.form['nuevaPalabra']
    tipo = request.form['tipo']

    # resultado_filtro = collectionPalabra.find( {'palabra':f'{nuevaPalabra}'} )

    # print(list(resultado_filtro))

    # if resultado_filtro != {}:

    #     return render_template('palabras.html', palabra_existe=True)

    # else:

    validacion = collectionPalabra.find( {'palabra':f'{nuevaPalabra}'} ).count()

    if validacion == 0:

        

        dic_tipos = {
            'naturaleza':False,
            'objetos':False,
            'animales':False,
            'romance':False,
        }

        dic_tipos[tipo] = True

        collectionPalabra.insert_one( {'palabra':f'{nuevaPalabra}', 'tipo':dic_tipos} )
    else:

        return render_template('palabras.html', palabra_existe=True)

    return render_template('palabras.html')

#******************************************
@app.route('/historialPalabra')
def historialPalabra():

    return render_template('historialPalabra.html')

#******************************************
@app.route('/historialPalabra', methods=['POST'])
def historialPalabraDatos():

    dic_tipos = {
            'naturaleza':False,
            'objetos':False,
            'animales':False,
            'romance':False,
        }

    listaPalabras = []

    tipo = request.form['tipo']

    # historial = collectionPalabra.find( {'tipo':f"{dic_tipos[tipo]}"}, {'palabra':1, '_id':0} )

    historial = collectionPalabra.find( {'tipo':{'$eq':tipo}}, {'palabra':1, '_id':0} )

    #* como lo hizo el profe 

    # historial = collectionPalabra.find( {'tipo':{'$eq':tipo}}, {'palabra':1, '_id':0} )


    # print(list(historial))

    for i in historial:

        for llave, valor in i.items():

            print(llave, valor)
            listaPalabras.append(valor)


    return render_template('historialPalabra.html', listaPalabras=listaPalabras)

#******************************************
@app.route('/eliminarPalabra')
def eliminarPalabra():

    return render_template('eliminarPalabra.html')


#******************************************
@app.route('/eliminarPalabra', methods=['POST'])
def eliminarPalabraDatos():

    palabraEliminar = request.form['palabraEliminar']

    resultado_filtro = collectionPalabra.find( {'palabra':f'{palabraEliminar}'} )

    print(list(resultado_filtro))

    if resultado_filtro != {}:

        collectionPalabra.delete_one( {'palabra':f'{palabraEliminar}'} )

    else:

        return render_template('eliminarPalabra.html', eliminado=False)


    return render_template('eliminarPalabra.html')

#******************************************

#* Crear rutas
#* En donde verficaremos si en mysql existe ese usuario.
#* Si no, enviar como alternativa al usuario a volver a intentar o a registrarse.
#* Si es registro, crear la SESSIOn con los datos del usuario.
#******************************************
@app.route('/')
def redireccionar():

    return redirect(url_for('home'))

#******************************************
@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        session.clear()

    if 'usuario' in session:

        return redirect(url_for('usuario'))

    return render_template('home.html')

#******************************************
@app.route('/usuario')
def usuario():

    return render_template('usuario.html')

#******************************************
@app.route('/usuario', methods=['GET', 'POST'])
def usuariodatos():

    if request.method == 'POST':

        try:
            usuario = request.form['usuario']
            password = request.form['password']

            #* IMPORTANTE: cADA VEZ QUE HAGAS UNA QUERY HAY CREAR UN NUEVO OBJETO
            bd = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
            #* #* Comprobar en mysql si existe el email
            leer_usuario = bd.query(
                f'SELECT usuario from usuarios WHERE usuario="{usuario}"'
            )

            print(leer_usuario)

            #* Si en la BD no esta vacio, entonces el email que se ingreso en el input existe en la BD
            if leer_usuario != ():

                # * Segunda comprbacion si la primera esta bien
                # *Comprobacion de email y password en la misma tupla.
                bd_total = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
                leer_usuario_password = bd_total.query(
                f'SELECT usuario, contrasenya, id_usuario FROM usuarios WHERE usuario="{usuario}"'
                )

                print(leer_usuario_password)


                bd = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
                #* Comprobar en mysql si existe la constraseña
                #* No necesita estar en un codicional, ya el condicional te lo hace el WHERE
                leer_password = bd.query(
                f'SELECT contrasenya from usuarios WHERE contrasenya="{password}"')

                print(leer_password)

                #* Si el email y la contraseña de la BD son igual al email y contraseña de los inputs. Redireccioname a dentro.html
                if leer_usuario_password[0][0] == usuario and leer_usuario_password[0][1] == password:
                    #* iniciar sesion 
                    #* Limpiamos la session cada vez que haga una nueva session.
                    session.clear()
                    session['usuario'] = leer_usuario_password[0][0]
                    session['password'] = password
                    session['id'] = leer_usuario_password[0][2]

                    return redirect(url_for('ahorcado'))

                else:
                    return render_template('usuario.html', no_usuario=True)
            else:
                return render_template('usuario.html', no_usuario=True)

        #* IndexError nos permite manejar el error cuando el email no esta en la base de datos.
        except IndexError:

            return 'No existe el usuario en la base de datos'

    return render_template('usuario.html')



#******************************************
@app.route('/registro')
def registro():

    return render_template('registro.html')


#******************************************
@app.route('/registro', methods=['GET', 'POST'])
def registroDatos():

    if request.method == 'POST':

        usuario = request.form['usuario']
        password = request.form['password']

        bd = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')

        leer_usuario = bd.query(
                f'SELECT usuario from usuarios WHERE usuario="{usuario}"'
        )


        print(leer_usuario)

        if leer_usuario != ():

            return render_template('registro.html', usuario_existe=True)

        bd2 = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
        #* Insertar tupla
        insertarTupla = bd2.query(f'INSERT INTO usuarios (usuario, contrasenya, activo) VALUES("{usuario}", "{password}", 1);')

        return redirect(url_for('usuario'))

        

    return render_template('registro.html')

#******************************************

# lista con palabra randomSQL en oculto, esto para cuando pulsen y se active el POST, este se reemplazara por el randomSQL de la ruta
@app.route('/ahorcado', methods=['GET'])
def ahorcado():

    if 'usuario' in session and 'password' in session:

        usuario = session['usuario']
        password = session['password']

    else:
        usuario = ''
        password = ''

    
    return render_template('ahorcado.html', imgAhorcado='inicio', password=password, usuario=usuario, randomSQLOculto=randomSQLOculto)

#******************************************

palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']
nuevoRandom = random.choice(palabras)

listaImagenes = ['inicio', 'cabeza', 'torso', 'brazoderecho', 'brazoizquierdo', 'piernaderecha', 'pierdes']

#* Objeto para sacar la palabra de la BD aleatoriamente.
objrandom = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')

#*Palabras Random con SQL
randomSQL = objrandom.query("""SELECT palabra FROM palabras ORDER BY RAND() LIMIT 1;""")

print(f'RANDOM SQL: {randomSQL[0][0]}')

randomSQLOculto = ' | __ | ' * len(randomSQL[0][0])

# queryPuntuacion = objrandom.query(""" SELECT u.id_,p.puntos_max FROM usuario AS u  INNER JOIN puntuacion AS p ON u.id_usuario = p.id_usuario;""")

# print(f'queryVerificacion: {queryPuntuacion}')


@app.route('/ahorcado', methods=['POST'])
def ahorcadoDatos():

    # palabras = ['miedo', 'oscuridad', 'alegria', 'feliz']

    # palabraRandom = random.choice(palabras)

    letraInput = request.form['letra']
    
    activar = request.form['activar']
    

    # objLetra = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')
    # objLetra = Ahorcado()
    objLetra = Ahorcado('localhost', 'usuario', 'mysql', 'ahorcadito')

    (listaLetras, imagenAhorc, aciertos, fallos, record) = objLetra.ahorcadito(letraInput, activar, randomSQL[0][0])

    print(f'ListaLetras: {listaLetras}')

    print(f'img Ahorcado: {imagenAhorc}')


    #***********************


    if 'usuario' in session and 'password' in session and 'id' in session:

        usuario = session['usuario']
        password = session['password']
        id_usuario = session['id']

    else:
        usuario = ''
        password = ''
        id_usuario = ''
        

    #***********************

    # queryPuntuacion = objLetra.query(""" SELECT u.nombre,p.puntos_max FROM usuario AS u  INNER JOIN puntuacion AS p ON u.id_usuario = p.id_usuario;""")


#* registro Puntuacion. En el ID_PUNTUACION sera el mismo que el id_usuario para que no nos duplique
# registroPuntuacion = objrandom.query(f'INSERT INTO puntuacion (id_puntuacion, id_usuario, record, aciertos, fallos) VALUES({id_usuario}, {id_usuario}, {record}, {aciertos}, {fallos});')


#*****************************
    # queryPuntuacion = objLetra.query(""" SELECT u.nombre,p.puntos_max FROM usuario AS u  INNER JOIN puntuacion AS p ON u.id_usuario = p.id_usuario;""")

    #***********************

    return render_template('ahorcado.html', random=randomSQL[0][0], letras=listaLetras, imgAhorcado=imagenAhorc, aciertos=aciertos, fallos=fallos, record=record, password=password, usuario=usuario)

#******************************************
#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)

