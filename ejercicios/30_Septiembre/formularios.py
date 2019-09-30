'''
FORMULARIO EN PYTHON CON ENTORNO VIRTUAL.

CONSEJO: DE LOS APUNTES QUE VIMOS SOBRE LOS PAQUETES, ESTOS PAQUETES NOS PUEDEN AYUDAR PARA EL BACKEND DE LA WEB
AL PONER EL CODIGO QUE CREAMOS Y COMPROBAMOS EN CONSOLA, LO PONEMOS EN UN PAQUETE Y YA EN MAIN.PY LO PODEMOS IMPORTAR COMO
SI FUERA UNA LIBRERIA, PAARA LLAMAR A LAS FUNCIONES MAS LIMPIAMENTE SIN TENER QUE METER EL CODIGO EN MAIN.PY

'''

# Creamos el formulario en un archivo a parte para que nos quede mas comodos
# Para despue importarlo en main en la APP:ROUTE(/), que queramos.

# lBRERIA BASICA DE FORMULARIOS

# Importamos el WTFORMS

# Importamos los inputs con sus tipos
from wtforms import Form, StringField, PasswordField, DateField, TextField, validators

# Importamos un imput para email
from wtforms.fields.html5 import EmailField

# NecesitaMOS UNA CLASE PARA TRABAJAR CON FORMULARIOS
# ESTA CLASE HEREDA DE LA CLASE FORM QUE HEMOS IMPORTADO

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

    # *************************************************************************

# Ya en main, en la ruta que queramos, importamos el archivo donde creamos el formulario

import formularios

# Para ya despues dentro de la ruta

@app.rout('/')
def home():

    # Creamos el objeto que albergara la clase importaba del archivo Formularios

    contactar = formularios.formularioContacto()

    # Lo introducimos dentro del RENDER_TEMPLATE

    return render_template('home.html', contactar=contactar)

    # ******************************************************************************************

# Ya en el archivo html donde enviamos el objeto

{{ contacto }}

# ********************************************************************************************

# Aunque podemos crear una macro para el formulario para tenerlo mas comodo

{% macro formularioContacto(campo) %}


{{ campo.label }}

# El '**kwargs' es un diccionario de argumentos, el cual le estamos diciendo    que nos convierta todo el contenido
# de la clase formularioContacto nos lo convierta en html. Los que hace es que los input al ser inlines, SAFE nos permite
# cambiar esto para poder hacer la conversion correctamente.

{{ campo(**kwargs) | safe }}

# Tambien podemos gestionar los errore,s por si el usuario no introdujo bien la informacion en los input
# en donde lo ponemos con 'campo.errors',  a su vez, con el FOR podemos generar un bucle para tener cada uno de los errores.
# y en este caso imprimirlos con un <h1>. 

{% if campo.errors %}

    {% for error in campo.errors %}

    <h1> {{ error }}</h1>

    {% endfor %}

    {% endif %}

{% endmacro %}

# ***************************************************************************************************

# Y ya cuando tengamos la macro, la importamos dentro del archivo hlhtml que queremos

{% form 'macro.html' import formularioContacto() %}

# ponemos la etiqueta FORM, para cuando la llamameos podamos enviar la informacion

<form action="" method="POST">

# contactar.nombreInput: Usamos el 'contactar' que proviene del render_template que hemos creado para poder llamar los inputs
# Ponemos los parametros que solo tenemos uno, y el cual va a ser el input, en este caso el input NOMBRE

{% formularioContacto(contactar.nombre) %}

# Obviamente necesitamos los otros input por lo cual, llamamos la funcion para crear de nuevo lo que tiene la funcion
# pero esta vez con el siguiente input. Y asi vamos llamando la funcion segun los inputs que tengamos

{% formularioContacto(contactar.email) %}

{% formularioContacto(contactar.comentario) %}

</form>


# ************************************************

# Ya en main.py de nuevo, en la tura donde tenemos el objeto con el formulario
# Ponemos los metodos de envio que usaremos en esa ruta, si no los ponemos, por defecto
# FLASK lo envia con GET no con POST

@app.route('/', methods=['GET', 'POST'])
def home():

    # Creamos el objeto que albergara la clase importaba del archivo Formularios
    # Ponemos en el constructor del objeto de la clase del formulario, el 'request.forms' es el que
    # recoge la informacion enviada con el <form>, lo que hace es al tener la informacion en el objeto
    # podemos usar el DATA para poder imprimir/usar/lo queramos con la informacion que recopilo 'request.forms'
    contactar = formularios.formularioContacto(request.forms)

    # Condicionamos la informacion que nos llega del methods del <FORM>:

    if request.forms = 'POST' and validators:

        # En este caso queremos imprimir, para verficar si ya llego la informacion

        print(contactar.nombre.data)
        print(contactar.email.data)
        print(contactar.comentario.data)

    else:
        print('Error en el formulario')

    # Lo introducimos dentro del RENDER_TEMPLATE

    return render_template('home.html', contactar=contactar)

# ****************************

# *** CREAMOS UN HONEY-POT **********

# En formularios.py

# Ademas creamos una clase especifica para HONEYPOT
# Cuando creamos nuestros propios VALIDATORS como el HONËYPOt, tenemos que hacerlos con funciones no con CLASS
# con Form para que la funcion se asocie con el formulario

def honeypot_len(Form, field):

    if len(field.data) > 0:

        # Validador de errores, es como TRY-EXCEPT

        raise validators.ValidationError('El campo debe estar vacio')

# en la clase del formulario ponemos un input que alberga el honeypot

# HIDDENFIELD: Es un input oculto, llamamos a laclase y la ponemos dentro del HIDENFIELD.
# Dejamos el '' porque estos son el label

# No hay necesidad de colocarle los valores a los parametros, ya que los VALIDATORS no necesitan

honeypot = HiddenField('', [honeypot_len])


# ************

# en el archivo donde importamos el MACRO con la funcion del formulario.

# Ponemos dentrop del <form>

{% form.honeypot %}


