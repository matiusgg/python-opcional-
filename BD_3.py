'''
SI ABRIMOS OTRO ARCHIVO COMO ESTE Y EN la variable "conexion" ponemos el nombre de una base de datos
ya conectada, podremos seguir haciendo creaicones, peticiones, actualizaciones, eliminar, etc.
sin problemas, ya que no influye el archivo .py en el que estemos trabajando sino el nombre de la BD
que estamos usando y poniendo en la variable "conexion"
'''

#* Importamos SQlite
import sqlite3

#* Para conectar la base de datos:
#* 1. Abrir la conexion, ponemos dentro de sqlite3.connect(nombreBD)
conexion = sqlite3.connect('segundaBD')


#* 2. Crear cursor(). El cursor nos permitira navegar A TRAVEZ DE La base de datos
cursor = conexion.cursor()

#* 3. Zona de SQL, donde desarrolla la creacion, actualizacion, eliminar, etc. tablas, atributos, INSERTAR DATOS

#****************CRUD******************


#* Leer informacion BD
cursor.execute('SELECT * FROM productos WHERE tipo="Deportes"')

#* Lista conversion, AL TENER UN QUERY ANTERIOR QUE CONDICIONA LA INFORMACION, LA LISTA
#* CONERTIRA LA INFORMACION DEL QUERY ANTERIOR NO TODAS LAS TUPLAS
listaDeportes = cursor.fetchall()

print(listaDeportes)

#*UPDATE
cursor.execute('UPDATE productos SET precio=300 WHERE producto="Zapatos"')

#*DELETE
cursor.execute('DELETE FROM productos WHERE producto="Peine"')


conexion.commit()








#* 2. Cerrar la conexion
conexion.close()