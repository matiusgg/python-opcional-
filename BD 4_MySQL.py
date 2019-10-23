'''
Descargamos en la consola pip install pymysql
PASOS: 
1. En la consola pip install pymysql
2. Pon en la variable conexion pymyswl.connect('localhost', 'root', 'mysql', 'nombreBD')
3. Abre la consola y abre el mysql para ir verificando si los QUERYS funcionan antes de
probarlos con python
4. Conecta la BD del mysql al sqlTOOLS en la opcion de MYSQl, rellena la informacion
5. Conecta la BD, si no te funciona es porque el MYSQL tiene por defecto un localhost diferente
por lo cual usando el comando en la consola en mysql:
ALTER USER 'root'@'nombreLocalHost' IDENTIFIED WITH mysql_native_password BY 'ponerContraseña';
nos permitira cambiar el localhost que queramos, en este caso en "nombreLocalHost" es el que pusimos en
"conexion", osea 'localhost'. Intentamos conectarlo de nuevo, y nos dara, ahora podremos hacer los querys sin problemas
y lo que queramos
'''

#* Importamos PYMSQL
import pymysql
import os

#* Para conectar la base de datos:
#* 1. Abrir la conexion, ponemos dentro de sqlite3.connect(nombreBD)
#* CONECTAR A BS MYSQL
conexion = pymysql.connect('localhost', 'root', 'mysql', 'libreriatoni')


#* 2. Crear cursor(). El cursor/lector nos permitira navegar/leer(la informacion) A TRAVEZ DE La base de datos
cursor = conexion.cursor()

#* ZONA SQL

#*Quiero listar a todas las clientas que se llamen maria
# cursor.execute('''
#     SELECT name  
#     FROM clients 
#     WHERE name LIKE "%Mar_a%"
# ''')

# listaMarias = cursor.fetchall()

# print(listaMarias)

# for maria in listaMarias:

#     print(maria)

#* Los uaurios puedan ver los escritores por nacionalidad

#* Hecho por mi

# cursor.execute('SELECT name, nationality FROM authors ORDER BY nationality')

# usuario = input('Introduce la nacionalidad y deescrubre cuales autores son de esa nacionalida: ')

# listaAuthorNat = cursor.fetchall()

# # print(listaAuthorNat)

# for author in listaAuthorNat:

#     autor = author[0]
#     nacionalidad = author[1]

#     if usuario == nacionalidad:

#         print(autor)

#* Hecho por el profe

#* Para ahorrarnos el condicional podemos poner el QUERY en una variable en esta
#* podemos usar el f'{}' para poner el input y que ya directamente el WHERE haga
#* el condicional en vez del IF de python, es decir, al hacer esto el WHERE nos hace el
#* condicional de una vez,
#* para despues ponerlo en EXECUTE()

while True:
   #usuario
   usuario = input('Nacionalidad: ')
   #* Como vemos el {0}, es la variable que tiene el input que colocamos mediante el FORMAT
   sql = "SELECT * FROM authors WHERE nationality = '{0}'".format(usuario)
   #* Seria lo mismo haciendo:
#    sql = f"SELECT * FROM authors WHERE nationality = '{usuario}'"
   os.system('cls')
   cursor.execute(sql)
   #conversion
   resultado = cursor.fetchall()
   for linea in resultado:
       id = linea[0]
       name = linea[1]
       nation = linea[2]
       # imprimir
       print(f'{nation} - {name}')
       
#* 4. Aceptar/Generar los QUERYS con:
conexion.commit()








#* 2. Cerrar la conexion
conexion.close()