#inicializamos la libreria básica de formularios

from wtforms import Form, StringField, TextField, validators, HiddenField
from wtforms.fields.html5 import EmailField #autovalidacion de html5

#generamos validadores, cosas propias dentro de formularios, mediante una  funcion
#declarar nuevas funcionaes validadoras pro

def honeypot_len(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe de estar vacío')

#necesito una clase para poder trabajar con formularios
# Esta clase hereda de la clase Form
class formularioContacto(Form):
    nombre = StringField('nombre: ', [
        validators.Required('Requerido'),
        validators.length(min=2, max=30, message ='Nombre no Válido')
    ])

    email = EmailField('correo electrónico: ',[
        validators.Required('es obligatorio'),
        validators.Email('Ingresar mail valido')
    ])

    comentario = TextField('comentario: ', [
        validators.length(min=10, max=200, message ='Comentario se excede del limite permitido')
    ])

    #TARRO DE MIEL , SEÑUELO, PARA LOS ROBOTS, que un robot rellena todos los campos una y otra vez . Esto es un campo que no se ve , Si alguien introduce informacion en un campo que no se ve, es que es un robot
    honeypot = HiddenField('', [honeypot_len])

