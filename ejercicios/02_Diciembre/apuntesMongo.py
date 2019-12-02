"""
DRIVER: El DRIVER es lo que permite la unión entre la BD y python. Por lo cual no necesitamos hacer ninguna clase.
PYMONGO(DRIVER): Es una libreria que hace la conexion, querys por mi.
NOS VAMOS A ATLAS DE MONGODB:
Y en el menu de atlas->clusters, en los "..." ponemos Load Sample Dataset y generamos BD de ejemplos
Despues nos vamos al Compass.exe
Compass es un visro, 
contraseña de la organizacion PROYECTO 0: mongodb
Ahora en Compass, concetamos la BD del atlaS Y tendriamos los _BD de ejemplo. Si nos vamos a SHECMA: veremos estadisticas de la BD.
Si damos click en alguna de las estadisticas nos filtrara ese dato para que nos busque como si fuera un query,
En la opcion del buscador si ponemos en PROJECT, atributos que queremos que salgan, tenmos que indicar:
{poster:1._id:0} Donde con 1:muestramelo, mientras que 0:no lo muestres
Ver el archivo mongo.txt para continuar:
Y en FILTER: Podemos filtrar a un documento embebido como:
{contacto.email:"pepetorres@gmail.com"}

CONECTAR ATLAS CON PYTHON
Ya en nuestro proyecto, en requirements ponemos 'pymongo' o en la temrinal: pip install pymongo

"""

from pymongo import MongoClient

#* CONSTANTE si nos interesara conectar nuestro mongo db en local
MONGO_URL_LOCAL = 'mongodb://localhost'

#* CONSTANTE CON
#* Para ello nos vamos a atlas->conectar->conectar a tu aplicacion
#* ejemplo: 'mongodb+srv://matius:<password>@primercluster-hewbh.mongodb.net/test?retryWrites=true&w=majority'
MONGO_URL_ATLAS = 'mongodb+srv://matius:mongodb@primercluster-hewbh.mongodb.net/test?retryWrites=true&w=majority'

#* MONGOCLIENT: Nos hara la conexion a altas
#* ssl_cert: Es el request que necesita la conexion pero como no lo tenemos, entonces lo desactivamos
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

#* Creacion objeto de la clase MONGODB
#* Mongo cuando no tiene una base de datos la crea, por lo cual no nos dara problema y a su vez, directamente usa esa base de datos.
db = client['pruebaDatos']
#* Creacion coleccion
#* Pasa lo mismo, si no esta la crea, y nos adentra dentro de ella.
collection = db['productos']

#*SRV: Viene junto a la MONGO_URL_ATLAS que permitira la conexion, por lo cual cuando estemos en el compat haciendo la coneccion,
#* tenemos que activar la opcion SRV
#* y para que la usamos en python, importamos la libreria en la consola: pip install pymongo[srv]


#* Creamos el primer documento
#* INSERT_ONE: Nos permite insertar un documento, esto viene del driver no de python
collection.insert_one( {'name':'Pepe', 'edad':44} )

#* y ya en compass y atlas verificamos si se creo la coleccion y BD.

#* Crear varios documentos
lista_Documentos = [
    {
        "producto": "lampara",
        "marca": "IKEA"
    },
    {
        "producto": "cama",
        "marma": "Picolin"
    }
]

#*INSERTMANY: nos permite insertar varios documentos
collection.insert_many(lista_Documentos)

#*IMPORTANTE: Si das a play, se te van a volver a introducir o ejecutar los querys que tengas, ponlos en comentarios un momento
#* para evitar que se nos dupliquen

#* LECTURA DE LOS DOCUMENTOS
#********************************************************************************************************************************

#* Leer todos los documentos de la coleccion
resultados = collection.find()
#* Lo convertimos en una lista porque sino nos lo lanza como un objeto al ser un documento
print(list(resultados))
for i in resultados:
    print(i)


#* Leer todos los documentos de la collection con un filtro
resultado_filtro = collection.find( {'producto':'cama'} )
for i in resultado_filtro:

    print(i)

#* Contar cantidad de documentos
resultado_contar = collection.count()
print(resultado_contar)

#******************************************************************************************

#* Actualizar un documento
#*SET: Actualizar a
collection.update_one( {'producto':'cama'}, {'$set':{'marca':'Piccolin'}} )

#* Actualizando incrementando un dato
#* $INC: Nos ayuda a incrementar un valor entero
collection.update_one( {'name': 'Pepe'}, {'$inc':{'edad':1}} )

#* con UPDATE_MANY: Que basicmente en vez de solo uno, nos actualizaría todos los que tenga esa condicion que pusimo dentro de los ().
collection.update_many( {'name': 'Pepe'}, {'$inc':{'edad':1}} )

#*******************************************************************************************

#* Borrar un documento

collection.delete_one( {'producto': 'lampara'} )

#* Borrar todos los documentos de una coleccion
collection.update_many( {} )
