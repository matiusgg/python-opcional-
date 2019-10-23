'''
Es una base de datos ligera, es conocida por android, y se emplea para integrarlas dentro de un proyecto, no es como
mysql, sino que se integran directamente dentro del proyecto.
TABLET plus es como un workbench de mysql

'''

#* Importamos SQlite
import sqlite3

#* Para conectar la base de datos:
#* 1. Abrir la conexion, ponemos dentro de sqlite3.connect(nombreBD)
conexion = sqlite3.connect('segundaBD')


'''
Descargamos e plugging "sqlTools"
Vamos a la extension y vamos a crear nueva conexion que tiene un simbolo de BD
vamos a la opcion de SQLite(Node Native)
Ponemos el nombre de la BD que pusimos en sqlite3.connect() y en Database File ponemos el archivo de BaseDatos no el de python,
ponemos SAVE CONNECTION
ponemos Conectar
Nos pedira la constraseña, que por DEFAULT de SQLITE3 es "admin"
Nos pedira que instalemos otro plugging para que funcione sqlTools correctamente,
lo instalamos y nos pedira conectar la baseDeDatos, damos que si, y
'''

#* 2. Crear cursor(). El cursor nos permitira navegar A TRAVEZ DE La base de datos
cursor = conexion.cursor()

#* 3. Zona de SQL, donde desarrolla la creacion, actualizacion, eliminar, etc. tablas, atributos, INSERTAR DATOS

#****************CRUD******************

# cursor.execute('''
#     CREATE TABLE productos(
#         producto VARCHAR(30) PRIMARY KEY,
#         precio INT(3),
#         tipo VARCHAR(20)
#     )
# ''')

# varios= [
#     ('Camiseta', 23, 'Deportes'),
#     ('Zapatos', 123, 'Deportes'),
#     ('Bolsos', 100, 'Moda'),
#     ('Peine', 5, 'Cosmetica')
# ]
# #* Insertamos las tuplas en la tabla
# cursor.executemany('INSERT INTO productos VALUES(?,?,?)', varios)

#* Leer informacion de la BD
cursor.execute('SELECT * FROM productos')

#* CONVERTIR LA INFORMACION de la BD EN UNA LISTA, para pdoer manipularla en python
listaProductos = cursor.fetchall()
print(listaProductos)

# Bucle para listaProductos
for producto in listaProductos:

    print(f'Articulo: {producto[0]} - Seccion: {producto[2]} - Precio: {producto[1]}')

conexion.commit()








#* 2. Cerrar la conexion
conexion.close()