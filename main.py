from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
# Libreria para protegernos de ataques de terceros
from flask_wtf import CSRFProtect
# paquete registro, para importar la clase Registro
from registro.registro import Registro

app = Flask(__name__)

# VAMOS A DECIRLE A LA APP QUE TENGA UNA PALABRA SECRETA. Nos servira
app.secret_key = 'palabra_muy_secreta'

csrf = CSRFProtect(app)

@app.route('/')
def index():

    return render_template('index.html')
    


@app.route('/registro', methods=['GET', 'POST'])
def datos():

    registro_form = Registro(request.form)

    if request.method == 'POST' and registro_form.validate():

        global informacion

        datoNombre = registro_form.nombre.data
        datoApellidos = registro_form.apellidos.data
        datoEmail = registro_form.email.data
        datoPassword = registro_form.password.data
        datoDireccion = registro_form.direccion.data
        datoLocalidad = registro_form.localidad.data
        datoNacionalidad = registro_form.nacionalidad.data
        datoDni = registro_form.dni.data


        informacion = {}
        

        informacion['datoNombre'] = datoNombre
        informacion['datoEmail'] = datoEmail
        informacion['datoApellidos'] = datoApellidos
        informacion['datoPassword'] = datoPassword
        informacion['datoDireccion'] = datoDireccion
        informacion['datoLocalidad'] = datoLocalidad
        informacion['datoNacionalidad'] = datoNacionalidad
        informacion['datoDni'] = datoDni

        

        return redirect(url_for('login'))

    else:

        print('Error en el formulario')

    return render_template('registro.html', formulario=registro_form)

@app.route('/registro')
def registro():

    return render_template('registro.html')

@app.route('/login', methods=['GET'])
def login():


    return render_template('login.html', **informacion)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)