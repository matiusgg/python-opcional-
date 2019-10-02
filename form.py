from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class Login(Form):

    username = StringField('Introduzca el usuario: ', [
        validators.Required(message='El usuario es obligatorio'),
        validators.length(min=3, max=30, message='Te has pasado de la longitud del username permitida')
    ])

    password = PasswordField('password: ', [
        validators.Required(message='El password es obligatorio')
    ])
