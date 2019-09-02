'''

PYTHON DECORADORES:

Son funciones que a su vez añaden funcionalidades a otras funciones, es decir, se pegan a funciones añadiendoles esas funcionalidades.
DECORAR es añadir funcionalidades.

ESTRUCTURA DE UN DECORADOR:
Si tenemos tres funciones por ejemplo donde Funcion A recibe como parametro a B, para devolver C,
y siempre un DECORADOR se aplica a una funcion o metodo con el simbolo @

Los decoradores es CODIGO muy habitual en PYTHON y en sus FRAMEWORKS

'''



# Para meter una funcion dentro de otra funcion usamos FUNC dentor de los parametros,
# FUNC nos permiten que los decoradores funcionen, la funcion que tiene en sus parametros el FUNC es el que
# encapsula a la otra funcion que va a decorar a otra.
# La cuestion es: Que funcion se pone en FUNC?. La funcion que se pone es la que va a recibir la decoracion
# la cual es la que va despues del @

def proteger(func):

    # Funcion que va se va a encapsular dentro de proteger(func)

    def envolver(password):

        if password == 'muevete':
            # En esta caso si la contraseña es muevete, 
            return func()
        else:
            print('Contraseña Incorrecta')

        # RETURN ENVOLVER, sirve para indicar que vamos a RETORNAR la funcion que va a decorar, es decir, que esta funcion nos la
        # retorne en la funcion que va a recibir la DECORACION

        return envolver

# Usamos antes se la funcion donde queremos meter la decoracion, ponemos el @funcionQueDecora

@proteger
def proteger_login():

    print('Tu contraseña es correcta')


if __name__ == "__main__":

    password = str(input('Escribre tu constraseña: '))

    proteger_login(password)

# PYPI: (Python package index)
# Para usar un COMPOSEr por asi decirlo en PYTHON, es decir, repositorios de terceros. Necesitaremos una herramienta como
# PIP.Tenemos que instalarlo en https://pip.pypa.io/en/stable/installing/. Damos a get.pip.py. DAmos CONTROl + A para copiar todo el codigo.
# Volvemos a VSC, creamos un nuevo archivo dentro del proyecto. y copiamos dentro de el el codigo
# Para instalar el PIP en la consola CMD: python get-pip.py y asi lo tendriamos en el sistema  Operativo.
# si la queremos en la vewrsion 3, pondriamos python3 get-pip.py en el proyecto y comprobar con pip --version

'''
Para generar un entorno como xampp o mamp como en php. Estan las virtualizaciones, que nos ayudaran en esta tarea:
Para intalar la virtualizacion usamos: pip install virtualenv

Ahora vamos a crear un entorno virtual, creamos una carpeta llamada Servidor y ademas ponemos en la consola CMD: virtualenv nombreServidor --python=python3
si no nos da: Ponemos virtualenv nombreServidor y nos creara la CARPETA nombreServidor con todo los archivos del entorno.
Entramos con CD a la carpeta del entorno, Tambien CD en Scripts: y ponemos source Scripts/activate

PIP FREEZE: Nos permititra decir que librerias nos ha instalado

PIP INSTALL nombreLibreria. EJN: pip INSTALL flask: Esta libreria nos permtira crear una pagina web con python

TOUCH requirements.txt: Nos permitira crear un archivo requirements.txt. En este archivo pondremos las librerias que nos mostro
PIP FREEZE y lo pegamos en este archivo, esto para guardar cual verison tenemos actual en este archivo. Este archivo debe ir en nombreServidor no en Scripts
Si otra persona quiere participar o hemos perdido los archivos ponemos: pip install -r requirements.txt

Que hace FLASK: Lo que ahce es ponernos en condiciones de poder crear proyectos web.

La carpeta del PIP la tenemos que tener dentro de la carpeta Servidor que creamos al principio dentro del proyecto.
Podemos desactivar con el entorno virtual con: deactivate en la consola.
Las librerias se intalan en LIB->SITE_PACKAGES
'''