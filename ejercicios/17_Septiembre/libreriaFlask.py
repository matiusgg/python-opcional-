'''
COMO IMPLEMENTAR UNA LIBRERIA EXTERNA A FLASK
PONEMOS EN REQUIREMENTS.TXT: flask-bootstrap
RECORDAR ESTAR DENTRO DEL ENTORNO VIRTUAL PARA HACER ESTO, YA ESTAMOS TRABAJNDO CON EL
pip install -r requirements.txt: Cuando introduzcamos nuevas librerias poner este comando para instarlos
Nos vamos a la consola y ponemos pip install -r requirements.txt. Nos revisa todo, y ve que este no esta,
lo instalara.
Ahora ponemos pip freeze > requirements.txt, para que nos instale las demas librerias de bootstrap

from flask_bootstrap import Bootstrap: Lo ponemos en main.py para importar el bootstrap
Creamos una variable y le asignamos: Bootstrap(app). App: Seria la variable que inicializamos con Flask para las rutas


el bootstrap tambien trabaja con BLOQUES con el JINJA.
Ahora en layout.html/base.html donde tenemos nuestro modelo html, eliminamos codigo html basico y lo reeemplazamos
con bloques de ninja que importamos con el bootstrap, para llamar con JINJA
para extender el bootstrap, asi {% extends bootstrap/base.html %} o si en vez de base.html es layout.html
Tambien nos cargamos el head, para poner JINJA en ellos, ponemos: {% block head %}, y asi con el body, y añadimos un bloque
llamado content(que nos servira para albergar el <main>, aunque no es obligatorio), recodar saber donde los vamos 
ha cerrar, por lo cual la tabulacion nos viene bien
para diferencias entre un {% endblock %} y otro.
Despies de abrir el bloque de <head> ponemos el super() para que importemos el HEAD, del bootstrap
Ten en cuenta que los nombres que le pongamos en los bloques del JINJA, son etqiuetas del bootstrap que pasan por FLASK
y JINJa nos lo permte colocar
Un ejemplo seria algo asi:


{% extends 'bootstrap/base.html' %}
    
    {% block head %}

    {{ super() }}

    <title>
        {% block title %}
            
        {% endblock %}
    </title>

    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css')}}">

    {% endblock %}

    {% block body %}

            {% block navbar %}

            {% include 'navbar.html'%}

            {% endblock %}
    
    {% block contents %}

            {% block main %}

            {% endblock %}

    {% endblock %}

    {% endblock %}

PROBLEMAS CON LA COOKIE QUE TENEMOS

En el proyecto EntornoEnv, en donde tenemos la Ip como cookie que hicimos en main.py
En donde si inicalizamos el servidor, y nos vamos al navegador y ponemos click derecho
-> inspeccionar->applications->storage->Cookies. en donde podemos manipular la cookie, lo cual es peligroso
Por lo cual necesitamos increptar la IP. para ello, dentro de FLASK tenemos un modulo llamdo SESSION,
lo ponemos dentro del import del FLASK. Este session encriptara la IP, cuando la usemos.
Ir a el main.py del proyecto EntornoEnv para mirar como lo hicimos

LIBRERIA FLASK WTF: Esta especializada en renderizar formularios
Hacemos lo mismo que con bootstrap, escribimos en requierements.txt: flask-wtf
y hacemos los comandos antes mencionados. Nos tiene que aparecer junto al bootstrap, estas lbrerias:

autopep8==1.4.4
Click==7.0
colorama==0.4.1
dominate==2.4.0
Flask==1.1.1
Flask-Bootstrap==3.3.7.1
Flask-WTF==0.14.2
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
pep8==1.7.1
pycodestyle==2.5.0
visitor==0.1.3
Werkzeug==0.15.6
WTForms==2.2.1

Ahora en main.py, la importamos: from flask_wtf import FlaskForm

y tambien : from wtforms.fields import StringField, PasswordField, SubmitField. Que nos permite crear los campos de los Strings y del password

Ahora necesitamos algo que valide el login, para ello importamos: from wtforms.validators import DataRequired

En total, los import que necesitamos son hasta ahora:

from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


El codigo esta en main RECUERDA.

Ahora nos vamos a home.html del pryoecto EntornoEnv

Importamos: {% import 'bootstrap/wtf.html' as wtf %}. DE donde sale esta ruta?:
Flaks de por si tiene el bootstrap, y este bootstrap tiene en su codigo la opcion de WTF
por lo cual nos importara la estructura del WFT, lo cual nos ahorra codigo

Para crear un formulario rapido con WTF, ponemos {{ wtf.quick_form(claseQueCreamosParaElLogin) }}

IMPORTANTE: Si vamos a emplear en html el <FORM>, tene en cuenta que flask por default, solo
afecta al metodo de envio GET, no POST por lo cual ponemos en el metodo de la ruta:

@app.route('/home', methods=['GET', 'POST'])

donde le decimos que los metodos de envio sean con get y con post

En main.py en el import de flask, importamos tambien url_for. Para que el condicional de validacion
del formulario puede ejecutarse. Lo enteras cuando veas el codigo del main.py en el proyecto

'''