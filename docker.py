'''
Buscar que es DOCKER en programacion y el concepto de entorno virtual
DOCKER: Contenedores,no son servidores, no es un entorno virtual

Ponemos mkdir para crear la acapreta serivodr y creamos dentro de esta el servidor, el virtual. Creamos otro entorno para hacer pruebas y no manchar el entorno principal.
Para entrar al entrono: source Scripts/activate
Para salir del entorno virtual: deactivate
PIP LIST: Nos muestra las librerias del proipo PIP, pero nos saca los Paquetes de las librerias, en cambio FREEZE nos lo da todo.
Tenemos que estar atentos a la version de PIP, si sale una verison nueva obviamente descartamos la que teniamos, y la actualizamos.
Para saber en que version hemos creado el PIP: pip --version
La diferencia con XAMPP o MAMP, es que estos usan un FRAMEWORK. En cambio FLASK no, auqneu puede usarlos.

Instruccione spara crear enytorno virtua:
1. instalaci0on pip: get-pip.py
2. Entramos a ala carpeta del proyecto y Verficar la verisond del PIP: pip --version
3. Creamos una carpeta donde va a estar el servidor: mkdir servidor y Entramos cd Servidor
4. cremoas dos entornos virtuales, uno de TEST para ahcer pruebas y otro donde lo usaremos para el proyecto: virtualenv venv/test
5. cd test
6. Para activar el entorno viretual source Scripts/activate
7. Para salir del entorno virtual: deactivate
8. Para Instalar Dependencias : pip install (Lo que quiera instalar. Ejm: flask). Si no sabemos el nombre podemos ir a buscar en google, pip. Nos saldra la pagina con un buscador(pypi.org). y buscamos la que queramos
9. pip freeze. Para verificar si se intalo.
10. Copiamos del freeze la linea de codigo con el nombre de lo que instalamos(ejm: freeze 1.1.1) y lo pegamos en requierements.txt
11. touch requierements.txt para crearlo y pegamos lo que copiamos.

Ahora vamos a usar el FLASK:
1. Vamos a la carpeta LIB->site_packages(Estan los paquetes de libreerias)-.
2. Creamos un archivo llamado index.py


'''