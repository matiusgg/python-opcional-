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
Ponemos el nombre de la BD que pusimos en sqlite3.connect() y en Database File ponemos el archivo de BaseDatos no el de python,
ponemos SAVE CONNECTION
ponemos Conectar
Nos pedira la constraseña, que por DEFAULT de SQLITE3 es "admin"
Nos pedira que instalemos otro plugging para que funcione sqlTools correctamente,
lo instalamos y nos pedira conectar la baseDeDatos, damos CONNECT NOW, y
VEREMOS EN EL PLUGGIN que las conexiones que tenemos, en donde veremos un enchufe rojo o verde,
el cual indica si la conexion esta encendido o no. esto viene bien si queremos
activar otra conexion de otra BD y apagar la conexion de la anterior BD.
'''

#* 2. Crear cursor(). El cursor/lector nos permitira navegar/leer(la informacion) A TRAVEZ DE La base de datos
cursor = conexion.cursor()

#* 3. Zona de SQL, donde desarrolla la creacion, actualizacion, eliminar, etc. tablas, atributos, INSERTAR DATOS
#* CRUD:Zona de sql mencionada en la linea de codigo anterior, cada vez que vayamos a hacer algo en el CRUD
#* es importante que vayaamos poniendo en comentario la anterior contenido, ya que cada vez que se ejecute
#* revisara todo de nuevo y vera que algunos ya fueron creados
#**************CRUD********************
# cursor.execute('''
#     CREATE TABLE prueba(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(30),
#         edad INT(3)
#     )
# ''')

# cursor.execute('''
#     INSERT INTO prueba VALUES(
#         NULL, "juan", 22
#     )
# ''')

#* Para inserar varios datos en la tabla
varios= [
    ('Pedro',34),
    ('Maria',4),
    ('Juan', 54)
]
#* Usamos el cursos para usar el sql, y con la funcion EXECUTEMANY()
#* nos permitira insertar varias tuplas a una tabla mediante una variable que
#* alberga las tuplas en una lista, en donde los "?"", serian equivalentes
#* a las posiciones de las tuplas de python que se introducen dentro del INSERT INTO
cursor.executemany('INSERT INTO prueba VALUES(NULL,?,?)', varios)


# #* 4. Aceptar/Generar los QUERYS con, debe ir 
conexion.commit()








#* 2. Cerrar la conexion
conexion.close()