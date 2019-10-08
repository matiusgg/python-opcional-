from flask import Flask, request, make_response, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
# paquete ofertas
from datosProductos.datos import Logica
# Setiembre 17: Crear otro template para cuando nos diga pagina no encontrada,
# lo dijiramos ese archivo html en la carpeta template

app = Flask(__name__)
boostrap = Bootstrap(app)


@app.route('/')
def redireccionar():

    return redirect('/home')


@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/home', methods=['POST'])
def productos():

    global dic
    global precios
    global calcCantidad
    global total

    dic = {}
    total = {}

    for i in range(10):

        producto = request.form[f'productos{i}']

        cantidad = request.form[f'cantidad{i}']

        dic[f'productoCant{i}'] = [producto, cantidad]

        objeto = Logica(producto, cantidad)

        precios = objeto.precioProducto()

        calcCantidad = objeto.calcular()

        total[f'precioTotal{i}'] = {

            'precio': precios,
            'total': calcCantidad
        }

    return redirect(url_for('bucle'))


@app.route('/bucle', methods=['GET'])
def bucle():

    return render_template('bucle.html', dic=dic, total=total)


@app.errorhandler(404)
def page_no_found(error):

    return '<h1> Pagina no encontrada, siga buscando</h1>'


if __name__ == "__main__":

    # Esto es para que cuando vayas a un localhost, tengamos esa ruta/url con
    # lo que le pusimos en app.run('0.0.0.0', '5000'). la idea es que FLASK
    # refleje PYTHON en un navegador
    # DEBUGEADOR para que que nos saque los fallos de bug
    app.run('0.0.0.0', '4000', debug=True)
