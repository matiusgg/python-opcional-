'''
Conectar una app a un servidor para introducir a BASE DE DATOS.
SDK: Son un grupo de libreriaS QUE NOS AYUDAN A CREAR SOFTWARE, nos ayudara a crear una app.
Usaremos el skd de google
Entramos : https://cloud.google.com/appengine/downloads
damos en PYTHON->y instalamos python 2.7.*(la mas actual) esto porque google en modo gratis no deja usar python 3
2. dar a descargar SDK
3. damos awindows o el quetengas, y lo instalamos
4. Cuando lo tengamos instalado, nos abrira el terminal en donde le damos "y" ara acceder, nos pedira que accedamos an nuestra
cuenta de gmail, y despues nos preguntara si queremos crear un proyecto, le damos si y le ponemos nombre, despues vamos a la direccion que nos coloca en la
terminal, donde tengamos el SDK, que google por predeterminado te pone en el nombre de la carpeta: google-cloud-sdk
5. Si descargamos un SDK sin instalador tenemos que instalarlo de esta manera, ponemos en el terminal ./install.sh para activar ese archivo
y nos lo instalara y nos preguntara lo de los pasos anteriores
6. ya en VSC, abrimos la carpeta con el SDK
7. En la temrinal accedemos a la carpeta del proyecto: google-cloud-sdk
8. Creamos un entorno virtual en la carpeta de nuestro proyecto que colocamos en el escritorio
8. Cuando lo tengamos, tengamos en cuenta que Google enginner no acepta el entorno virtaul de Pip. Por esta razon creamos una carpeta llamada lib dentro de la carpeta servidor
10. DEntro de servidor, creamos una rchivo llamado appengine-config.py. Dentro de este colocamos: Para indicarle donde empieza nuestro proyecto para importarle las librerias
de google.


from google.appengineext:
import vendor

vendor.add('lib')

11. Despues creamos otro archivo app.yaml: En donde le decimos como va a ser el servidor con google, es decir las caracteristicas que va a tener el servidor
y donde esta nuestro main.app es decir donde empieza la aplicacion

service: default
runtime: python27
api_version: 1
threadsafe: yes

handlers:
- url: .*
  script: main.app
  secure: always

12. Ponemos en la consola en servidor: pip install -r requirements.txt -t lib para que lo que tenemos en
requierements.txt, que eneste caso es el flask(si tienes otras librerias ponlas antes de hacer este paso),
lo installe en la carpeta LIB que creamos en la carpeta servidor. en donde -t es para introducir la instalacion dentro de LIB

13. dev_appserver.py . : Ponemos este comando para accder a google cloud. Tenemos que estar en python 2, por lo cual asegurate de cambiarlo.
Para no tener problemas con los PYTHON'S. Cuando instales el python 2, en la ventana de instalacion donde aparece opciones de instalacion
veras que tienes el path python 2, con una X. Si tienes python 3 antes de instalar python 2, este es el motivo por el que esa opcion te aparece con una X.
ya que el PATH por predeterminado esta con python 3, no con python 2 obviamente. Por lo cual cambia la opcion de la X, por la de activar el PATH de python 2.
Lo que hara basicamente es cambiar el PATH(ruta) del python 3 al python 2 cuando lo instales. Cuando ya tengas esto, Cambia el nombre del python 3,
por ejejmplo "python3", en la ubicacion del archivo donde tengas python 3. Esto para que cuando estes en la terminal, y coloques python solamente, te abra el python 2.
En cambio si poes python3 como lo nombraste anteriormente en tonces se abrira python 3 obviamente, Ahora vuelves a VSC o a la terminal donde estabas
y coloca dev_appserver.py . 
14. damos "y" para crear el servidor, y nos dara la direccion url
15. creamos en la carpeta servidor, el archivo main.py y lo colocamos en ella laconexion entre nuestros archivos html con las rutas con el FLASK

# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hola():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()


'''
