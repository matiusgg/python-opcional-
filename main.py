from flask import Flask, request, make_response, redirect, render_template

# FLASK es una clase, por eso sale con la primera letra en mayuscula
# request: permite recopilar datos, en este caso para sacaqr la ip
# make_response: Nos permite generar una respuesta
# redirect: Nos permite redireccionar al usuario a otra ruta
# render_tempalte: Con esta libreri apodemos renderizar las cosas que hagamos
# en las carpetas STATIc y en TEMPLATES

app = Flask(__name__)

# Si queremos enviar una lista al html, el n ombre de la variable de la lista
# la colocamos como llave en el diccinario,
# la idea es que podamos recopilar toda la informacion de la variables que
# queramos enviar para renderizar en el html
algunos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@app.route('/')
def redireccionar():

    # Dame la direccion de la IP del usuario, esto nos sirve para ponerle una
    # cookie y sacarle INFO.

    user_ip = request.remote_addr

    # Vamos a crear una RESPuesta y una REDIRECCION a la nueva ruta, es ecir
    # esto nos srive por si el usuario no sabe que la ruta ha cambiado a otra
    # donde con REDIRECT, te redijirije a /contactar

    respuesta = make_response(redirect('/home'))

    # Poner una cookie al usuario de su IP. Aqui significa que se coge la IP
    # del usuario metiendola en una cookie, esto cuando te redireccionemos
    # donde set_cookie('nombreCookie', variable que recopila la IP)
    respuesta.set_cookie('user_ip', user_ip)

    return respuesta

# {{}} {{}} ==


@app.route('/home')
def home():

    ip = request.cookies.get('user_ip')

    # Normalmente, cuando vamos a enviar variables a html, hay que tener en
    # cuenta que vamos a enviar muchas
    # variables por lo cual, usamos un diccionario para que nos acomode esta
    # tarea

    contenido = {
        'ip': ip,
        'algunos': algunos,
    }

    # Enb este punto con ** se despliega el diccionario para enviar la
    # informacion, es decir. Al momento de llamar el diccionario en los html 
    # con JINJA,
    # no colocar el nombre del diccionario, porque al ponerle ** lo estamos 
    # desplegando, por lo cual
    # podemos usar sus llaves para sacar los valores sin necesidad de poner el
    # nombre del diccionario

    return render_template('home.html', **contenido)

    # la forma corta de hacerlo, pero que no necesitamos porque queremos
    # enviar mucha informacion y no es viable

    # Ejm: return render_template('home.html', user_ip=user_ip)


@app.route('/contactar')
def contactar():

    # Obtener la IP del usuairo que previamente hemos almacenado en la cookie
    # cookies: Es un modulo de la libreria de request
    # get(): para recuperar la IP almacenada en la cookie

    # user_ip = request.cookies.get('user_ip')

    # print(f'Ya estas en Contactar!!! y la IP del usuario es: {user_ip}')

    return render_template('contactar.html')

# Manejamos el posible error de PAGINA NO ENCONTRADA, manejando el error a
# nuestro gusto,
# En este caso el error 404


@app.errorhandler(404)
def page_no_found(error):

    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    # Esto es para que cuando vayas a un localhost, tengamos esa ruta/url con
    # lo que le pusimos en app.run('0.0.0.0', '5000'). la idea es que FLASK
    # refleje PYTHON en un navegador
    # DEBUGEADOR para que que nos saque los fallos de bug
    app.run('0.0.0.0', '5000', debug=True)
