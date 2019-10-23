'''
Es una base de datos ligera, es conocida por android, y se emplea para integrarlas dentro de un proyecto, no es como
mysql, sino que se integran directamente dentro del proyecto.
TABLET plus es como un workbench de mysql

'''

#* Importamos SQlite
import sqlite3

#* Para conectar la base de datos:
#* 1. Abrir la conexion, ponemos dentro de sqlite3.connect(nombreBD)
conexion = sqlite3.connect('primeraBD')


'''
Descargamos e plugging "sqlTools"
Vamos a la extension y vamos a crear nueva conexion que tiene un simbolo de BD
vamos a la opcion de SQLite(Node Native)
Ponemos el nombre de la BD que pusimos en sqlite3.connect() y en Database File ponemos el archivo donde abrimos la conexion
ponemos SAVE CONNECTION
'''

#* 2. Crear cursor(). El cursor nos permitira navegar A TRAVEZ DE La base de datos
cursor = conexion.cursor()

#* 3. Zona de SQL, donde desarrolla la creacion, actualizacion, eliminar, etc. tablas, atributos

#**********************************
cursor.execute('''
    CREATE TABLE prueba(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(30),
        edad INT(3)
    )
''')


#* 4. Aceptar los QUERYS con:
conexion.commit()








#* 2. Cerrar la conexion
conexion.close()


