'''
SETUP:PY
NOs permitira decirle a python que es lo queremos ahcer con un paquete
para pdoer distribuir nuestro paquete en cualquier parte del mundo.
Si tenemos un paquete que creemos que puede ayudar, el SETUP nos permite distribuir el paquete como
una libreria en paginas ya sea github o la pagina de PIP PYTHON
El archivo debe estar afuera del paquete junto con MAIN.py
'''

#* Importamos la libreria SETUP
from setuptools import setup

#* Usamos SETUP donde pondremos los detalles de ese paquete y sus caracteristicas

setup(
    name='paquetecalculo',
    version='1.0',
    description='Paquete de ayuda con los calculos basicos',
    author='Matius',
    author_email='jaumecostagomez@gmail.com',
    url='jaumecosta.com',
    packages=['paquete_calc']

    #* PACKAGES: Es donde le diremos la ruta del paquete, es decir que al introducirle el nombre del
    #* paquete en PACKAGES, este albergara todos sus modulos sinproblema, pero si este paquete tambien tiene
    #* Subpaquetes entonces nos viene bien ponerlo en una lista para que tengamos todas las rutas tanto del paquete-padre
    #* como de los paquetes-hijos
)

#* Ahora en terminal ponemos py -3 setup.py sdist para introducir el setup del paquete dentro de python
'''
Nos creara dos carpetas, una llamada DIST, que albergara una carpeta comprimida que ayudara a la distribucion, y otra llamada nombredelPaquete.egg-info el cual
albergara la informacion que le hemos dado en el SETUP
'''