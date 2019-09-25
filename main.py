from flask import Flask, request, make_response, redirect, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SUPER SECRETO'


class loginForm(FlaskForm):

    anyo = StringField('Ingrese su anyo de nacimiento',
                       validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired])


@app.route('/')
def redireccionar():

    return redirect('/home')


@app.route('/home', methods=['GET', 'POST'])
def home():

    login_form = loginForm()

    if login_form.validate_on_submit():
        anyo = login_form.anyo.data
        session['anyo'] = anyo

        return redirect(url_for('home'))
    
    anyoSession = session.get('anyo')
        
    return render_template('home.html', anyoSession=anyoSession)


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
