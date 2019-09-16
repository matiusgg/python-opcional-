'''
PARA ACTUALIZAR EL PIP, USAMOS: pip install -U pip

PARA MIRAR LA VERSION:  pip --version

*************************************
OTRA FORMA DE CREAR UN ENTRON VIRTUAL ENV
*************************************

1. Creamos una carpeta y ponle en el nombre de la carpeta ENV junto al nombre que le pongas

2. No crees una carpeta SErvidor hazlo en la misma carpeta creada 

3. Pon en la consola: /python -m venv env // PYTHON por si solo puede virtualizar entornos, no necesita a travez de PIP
parta poder hacer la  virtualizacion. Donde VENV: seria la llamada a python para crear el entorno virtual

4. pon source env/Scripts/activate /7 Para sctivar el entorno virtual

5. Creamos un archivo afuera del entorno virtual, y VSC nos crea un JSON que alberga infromacion del entorno virtual

6. VSC nos dira que instalemos pep8, ponemos SELECT LINTER y escogemos pep8. Lo instalamos, pero nos aseguramos que estemos dentro del entorno virtual.

7. Comprobamos en la barra izquierda inferior si estamos en el entorno virtual

8. Comprobacion si se instalo pep8 en el entonrno virtual para ello nos aseguramos de que instalamos el pep8 dentro del entorno virtual
ponemos pip freeze y SOLO nos puede aparecer la libreria del PEP8

9. Para desisntalar cualquier libreria pon pip unistall nombreLibreria. En este caso, si no nos sale el pepe8, para despues repetir los pasos

10. Instalamos en el EV(entorno virtual) la libreria: pip install colorama

11. Ponemos el la consola: pip freeze > requirements.txt . Esyto es para que el requrements meta todas las librerias que necesitemos, dentro de su archivo para pdoer usarlas
El requirement sera como nuestro historial por si vamos a otro proyecto, podemos usar el requirements como base de nuestras librerias
que necesitemos

12. Ya en el archivo que habiamos creado importamos la libreria COLORAMa que instalamos:
from colorama import Fore, Back, Style

13. La diferencia con FLASK, es que flask nos permite interactuar con un serivodr como xampp. Por lo cual lo instalamos
pip install flask

14. vOLVEMOS A `PONER pip freeze > requirements.txt para que nos agregue al archivo requierement el Flask. Nos generara
mas librerias que no queremos por lo cual eliminamos:
pycodestyle==2.5.0
Werkzeug==0.15.6
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Click==7.0

CONSEJO: NO meter el proyecto como una subcarpeta, abrela con VSC para ese proyecto, no lo hagas estando en una carpeta mas grande

JiNJA: Nos permite interactuar renderizar HTMl con el PYTHON, donde creamos:

1. una carpeta llamada 'templates' fuera del entorno virtual.Donde vanmos a tener mayormente nuestro HTML
donde como en el anterior pryecto con entorno virtual, en el pondremos un layout.html que sera el html principal para los demas

2. Tambiewn otra llamada static. Vamos a tener mayormente img/, sass/LAs de STATIc como su nombre indica 

3. Para llamar una variable de PYTHON en HTML, usamos {{ variable }}. No pongas en los corchetes espacios entre uno y el otro, {{}}
'''

