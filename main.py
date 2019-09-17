from flask import Flask, request, make_response, redirect, render_template, session, url_for

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('home.html', )



@app.errorhandler(404)
def page_no_found(error):

    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    app.run('0.0.0.0', '4000', debug=True)
