from flask import Flask, request, render_template

#Importar nuestro archivo de formularios
import forms

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    #instanciar la clase de formulario
    #el  request nos recupere el objetoform
    contactar = forms.formularioContacto(request.form)

    # SI NOs envian algo por POST en la terminal y contactar.validate es True:  nos salen los datos del formulario
    if request.method == 'POST' and contactar.validate():
        print(contactar.nombre.data)
        print(contactar.email.data)
        print(contactar.comentario.data)
    else:
        print('error en el formulario')
        
    #dentro de usuario.html ya podemos utilizar el formulario que hemos creado
    return render_template('usuario.html', form=contactar)

# MODO UNO
# @app.route('/parametros')
# def param():
#     # http://127.0.0.1:5000/parametros?par=23
#     param = request.args.get('parametro', 'No hay parametro')
#     return (f'El parametro enviado es : {param}')

#MODO DOS definiir dos rutas con una misma función
# @app.route('/parametros')
# @app.route('/parametros/<otraruta>')
# @app.route('/parametros/<otraruta>/<int:numero>')
# def param(otraruta = '', numero = 0):
#     return (f'El parametro enviado es {otraruta} y {numero}')

#MODO TRES
# en la direccion tengo que poner localhost:5000/usuario/toni
@app.route('/usuario/<nombre>')
def param(nombre=''):
    menu = ['inicio', 'galeria', 'contactar']
    return render_template('usuario.html', usuario = nombre, menu = menu)

if __name__=="__main__":
    app.run('127.0.0.1', 5000, debug = True)