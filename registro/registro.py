from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class Registro(Form):

    nombre = StringField('Introduzca el nombre: ', [
        validators.Required(message='El nombre es obligatorio'),
        validators.length(
            min=3, max=30, message='Te has pasado de la longitud del nombre permitida')
    ])

    apellidos = StringField('Introduzca los apellidos: ', [
        validators.length(
            min=3, max=30, message='Te has pasado de la longitud del apellidos permitida')
    ])

    password = PasswordField('password: ', [
        validators.Required(message='El password es obligatorio')
    ])

    direccion = StringField('Introduce la direccion: ', [
        validators.length(
            min=5, max=80, message='Te has pasado de la longitud de la direccion permitida')
    ])

    localidad = StringField('Introduzca la localidad', [
        validators.Required(message='La localidad es obligatoria')
    ])

    nacionalidad = StringField('introduzca la nacionalidad', [
        validators.Required(message='La nacionalidad es obligatoria'),
        validators.length(
            min=2, max=3, message='Te has pasado de la longitud de la direccion permitida, son con 3 caracteres o menos')
    ])

    dni = StringField('Introduzca el dni: ', [
        validators.length(
            max=9, message='Te has pasado de la longitud del dni permitida, son maximo 9 digitos')
    ])

    email = EmailField('Correo Electronico: ', [validators.Required('Es obligatorio'),
                                                validators.Email('Ingresar su email valido')])
