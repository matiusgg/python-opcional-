from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from form import Login
# Libreria para protegernos de ataques de terceros
from flask_wtf import CSRFProtect

app = Flask(__name__)

# VAMOS A DECIRLE A LA APP QUE TENGA UNA PALABRA SECRETA. Nos servira
app.secret_key = 'palabra_muy_secreta'

# Llamaos a la funcion de CSRF y ponemos app
csrf = CSRFProtect(app)

# rutas
@app.route('/')
def index():

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = Login()

    return render_template('login.html', formulario=login_form)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
