'''
IMPORTANTE EN FLASK EN REDIRECT:
Si vamos a usar URL_FOR dentro del REDIRECT, la ruta a la que queremos redireccionar seria el nombre del funcion
que tiene la ruta a la que queremos ir. EJM:

@app.route('/')
def redireccionar():

    #* Como vemos no ponemos el nombre de la ruta '/contactar' sino el nombre de la funcion que alberga la ruta a la que
    #* queremos ir en este caso 'cont'
    return redirect(url_for('cont'))

@app.route('/contactar')
def cont():

    return rende_template('contactar.html')

*********************************************************************************************


SESSIONES EN PYTHON: La gestión que hace Flask de la sesiones, es no utilizar espacios
de memoria, sino que utiliza cookies.
'''

'''
    Necesitamos crear una cookie y cifrar su contenido, necesitar una clve/llave secreta
'''
#* Esto en main.py. Llave secreta
app.secret_key = 'mi_clave_super_secreta'

'''
Añadir contenido a una session. Lo que ahce basicamente es crear una variable en la session donde albergara la cookie.
------------------------------
session['nombre_variable_session'] = valor
'''

#* Supongamos que recogemos los datos de un input y lo ponemos en una session.
nombre = request.form['nombre']
apellido = request.form['apellido']
#* Ponemos lo inputs en la session.
#* Session va a guardando cada input en una cookie y no en memoria
#* Abrimos session.
session['nombre'] = nombre
session['apellido'] = apellido

#************************************************************
#* MOSTRAR CONENIDO/TRAER CONTENIDO DE LA SESSION
#* simplemente ponemos otra vez session['nombre_variable_session_que alberga_el_valor']
session['nombre']

'''
    SI QUEREMOS VALIDAR SI EXISTE UNA VARIABLE DENTRO DE UNA SESSION.
    Es decir, comprobar si esa variable de session hay un valor
'''
if 'apellido' in session:
    #* si es verdad asignamelo a una variable normal de python
    apellido = session['apellido']

'''
    CERRAR LA SESSION PARA QUE NO SE ACUMULE INFORMACION Y NOS PETE.
    QUE SIMPLEMENTE CUANDO TERMINE EL PROCESO DEL USUARIO
'''
#* Eliminar variables de la session si tenemos muchos datos pero no cerramos aún la session:
#* POP: podemos eliminar una variable de una session, eliminando esa cookie
session.pop('nombre', None)
session.pop('apellido', None)

#* Eliminar TODA la session:
#* Borra todas las variables y las cookies
session.clear()

#* Porque no usamos GET en un login, porque cuando enviemos los datos estos seran vistos en la URL y desprotegidas por
#* no estar encriptadas.
#*Lo que pasa con SESSIOn es que cada vez que vemos un nuevo template de flask,
#* esas cookies estaran encriptadas y en todos los templates.

#* Una nueva libreria para el entorno virtual es PYLINT
#* Para REDIRECCIONAR EN MAIN.PY NECESITAMOS IMPORTAR REDIRECT Y URL_FOR DE LA LIBRERIA DE FLASK