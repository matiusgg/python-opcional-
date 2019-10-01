from wtforms import Form, StringField, PasswordField, DateField, TextField, validators
from wtforms.fields.html5 import EmailField


class formularioContacto(Form):

    # Como vemos el VALIDATORS.LENGTH podemos usarlo para condicionar la informacion que nos van a instroducir
    # en este caso la longitud de la informacion del input

    nombre = StringField('Nombre: ', [validators.length(min=5, max=30, message='Nombre no valido, porque se excede del nombre permitido'),
                                      validators.Required('Es obligatorio')])

    # el EMAILFIELD sirve para introducir EMAILS

    email = EmailField('Correo Electronico: ', [validators.Required('Es obligatorio'),
                                                validators.Email('Ingresar su email valido')])

    # El TEXTFIELD sirve para hacer un comentario

    comentario = TextField('Comentario: ', [validators.length(min=10, max=200, message='Mensaje que se excede del limite permitido'),
                                            validators.Required('Es obligatorio')])
