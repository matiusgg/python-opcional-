from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def home():
   return 'Iniciando Web'

# *******************************************
@app.route('/parametros')
def param():
   http://127.0.0.1:5000/parametros?par=23
   param = request.args.get('par', 'No tenemos parametros')
   Envia esta variable llamada parametro
   return (f'El parametro enviado es: {param}')

# ***********************************************
@app.route('/parametros')
@app.route('/parametros/<otraruta>')
# el <> so  parametros que recibe la funcion
@app.route('/parametros/<otraruta>/<int:numero>')
def param(otraruta='', numero=0):enviar parametros a traves de rutas de flask
   return (f'El parametro enviado es: {otraruta} y {numero}')

# **********************************************
@app.route('/usuario/<nombre>')
def param(nombre=''):
   menu = ['inicio', 'galeria', 'contactar']
   return render_template('usuario.html', usuario=nombre, menu=menu)



   
if __name__ == "__main__":
   app.run('127.0.0.1', 5000, debug=True)