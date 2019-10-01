
from flask import Flask, request, make_response, redirect, render_template, session, url_for
from packForm.form import formularioContacto

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# **********************************************************************************************

# @app.rout('/')
# def home():

#     # Creamos el objeto que albergara la clase importaba del archivo Formularios

#     contactar = packForm.formularioContacto()

#     # Lo introducimos dentro del RENDER_TEMPLATE

#     return render_template('home.html', contactar=contactar)


# @app.route('/')
# def home():
    
#     global contactar

#     contactar = formularioContacto(request.form)

#     return render_template('home.html', contactar=contactar)

# *********************************************************************************************


@app.route('/', methods=['GET', 'POST'])
def home():

    contactar = formularioContacto(request.form)

    informacion = {}

    if request.method == 'POST' and contactar.validate():

        datoNombre = contactar.nombre.data
        datoEmail = contactar.email.data
        datoComentario = contactar.comentario.data

        informacion['datoNombre'] = datoNombre
        informacion['datoEmail'] = datoEmail
        informacion['datoComentario'] = datoComentario

    else:

        print('Error en el formulario')

    return render_template('home.html', contactar=contactar, **informacion)


# *********************************************************************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
