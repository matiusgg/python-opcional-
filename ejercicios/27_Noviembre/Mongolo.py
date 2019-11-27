"""
MONGODB: Es una BD NoSQL. Es una BD orientada a documentos, no sigue un esquema. Es decir, no se sigue el esquema
de las tablas sino que serían documentos, en lugart de guardart los datos en registros, guarda los datos en un documento
se llama BSON de documento Binario. La ventaja de MONGODB es que se adapta según nuestras neceaidades como NO es necesario
seguir un esquema como en Mysql que tenemos que tener los atributos ya definidos mientras que MONGO pongo agregar varios
registros con sus propios atributos sin influir en el otro.
Es una base de datos distribuida, no solo hablamos de un servidor . Le llamaremos "CLUSTER". Dnde po0demos "escalar" mediante un
CLuster principal a otro CLuster, Y DENTRO DE CADA clUSTER PUEDE HABER xcANTIDAD DE BASES DE DATOS, si nos quedamos conrto de almacenamiento
en un cluster, podemos ir al otro. Ademas de que podemos agregar mas cluster/mas servidores para labergar BD's. Esto nos beneficia en que
no se concentra en uno solo.
CARACTERISTICAS:
MongoDB Server: Donde guarda los datos:
1.enterprice: Version de pago, incluye novedades. Beneficia para una empresa
2.Community: Para la comunidad, codigo abierto
3.Atlas(con el que trabajaremos): Es un Cloud con Clusters. Lo emplearemos a travez de los ervidores de AMAZON. Necesita:
3.1 Shell: Terminal paara mongo
3.2. Compass: Interface
Resumen:
BD: Creamos colecciones no tablas, cada BD tiene su proipo sistema de archivos, un cluster puede tener multiples BD's
Colecciones: Agrupacion de documentos, estos vendrian a hacer una tabla de Mysql.
Documentos: Donde estan los registros(tupla) dentro de una coleccion. Este documento se crea a partir de un BSON.

Para descargar, ve a la pagina oficial de mongo DB:
1.Try-Free: Rellenamos los datos, nos enviaran un email para confirmar. Creamos un CLuster FREE, ponemos el de AMAZON
despues el FRANKFURT, alemania, y nombramos el cluster, y damos a Crear. Mientras se crea, damos en DataBase Access->creamos un nuevo Usuario.
Damos en Atlas Admin, ponemos nombre y contraseña(las tenremos que recodar)-> lo creamos
Vamos a Network Access->new ip adress(que sera nuestra IP global con la que trabajaremos)->tenemos dos opciones:
1.Current Ip(nos generara una ip publica) y una IP ANYWHERE. Damos a IP ANYWHERe, le agrtegamos un comentario y la creamos.
Vamos a CLUSTER->connect->connect with SHELL->descargamos Download Mongo Shell->extrayemos el descarga y nos dara una carpeta,
con la terminal de mongoDB.
Ahora ponemos la ruta bin de la terminal de mongo, y la ponemos en las variables de entorno del sistema, guardamos.
Abrimos el cmd, ponemos la ruta de bin, y ponemos mongo "mongodb+srv://primercluster-hewbh.mongodb.net/test"  --username matius
nos pediran password, y ya estaremos dentro.
Los DRIVERS: Son las libreias que nos van a ayudar a hacer esta coleccion. Algunas lenguajes que mongo brinda sus librarias son:
:c, c++, c#, python, motor(python), java,
php, ruby, mongoID, scala
en Cloud->Atlas->

ARQUITECTURA DE MONGODB:
FrontEnd-
Backend: Python, java, modejs, etc. EStos lenguajes tendran los drivcers para conectar la BD->: MongoDB. Tendriamos dos servicios de
administracion para trabajar con MONGODB: mongoSHELL, compass.

Cuando ya estemos en SHELL:
Para salir de mongo: exit
mostrar BD's: show databases
crear BD: use segundaBD
db: Para usar la BD(no podemos dejar una bd vacia.) por lo cual creamos la coleccion:
INSERTONE: Nos permite introducir un la coleccion en la BD. donde podemos poner diccionarios, listas, etc.
db.nombreColeccion.insertOne({datosColeccion})
Ejm:
db.nombreColeccion.insertOne({producto:"boli",cantidad:"200", etiquetas:["negro"],size:{altura:10, weight:2, tipo:"mm"}})
Si nos dale TRUE, e que lo hizo bien, Nos dara un objetoID: con el codigo de esa coleccion.
Para ponerle un objetoID de manera manual y no el que nos de MONGO ponemos:
db.nombreColeccion.insertOne({_id:"pruebaID",producto:"boli"...
FINDONE(): Nos permite ver un registro. Nos mostrara el primer "atributo" en este caso el objID. Si queremos filtrar:
db.nombreColeccion.findone({producto:"boli"}) Nos mostrara un resultado con ese filtro. Si queremos ver mas resultados con este filtro usamos:
db.nombreColeccion.find({producto:"boli"}) Si queremos usar count() para contar cuantos resultados tenemos:
db.nombreColeccion.findone({producto:"boli"}).count() Esto no nos funcionara con FINDONE: Por que obviamente sirve para un resultado.
FIND(): Para ver todo la coleccion
FIND().PRETTY(): Par aque nos lo deje mas bonito
show collections: seria como mostrar tablas/agrupaciones de documentos.
INSERTMANY: Sirve para insertar varias colecciones, estructura: insertMany([{coleccion1}, {coleccion2}, {coleccion3}])
db.nombreColeccion.insertMany()
Si hacemos una busqueda mediante el objID, sin haberlo cambaido manualmente ponemos el objID que nos dio MONGODB.

Para actualizar:
UPDATEONE: Nos permite cambiar un registro por otro en la coleccion, estructura: updateOne({antiguoAtributo}, {$set:{nuevoAtributo}})
Cambiar "rotulador" por "rotu":
db.inventario.updateOne({producto:"boli"}, {$set:{producto:"boligrafo"}})

UPDATEMANY: Nos permiote actualizar varios registros de la coleccion

db.inventario.updateMany({producto:"boligrafo"}, {$set:{producto:"boli"}})

DELETEONE: nos permite borrar un registro de la colección
db.inventario.updateMany({producto:"rotu"})
DELETEMANY: No recomendable usar por precaución. NUNA PERO NUNCA PONER: .deleteMany({}), ya que es inventario vacío

Vamos a la paghina de MongoDB y vamos a software->compass-> descargamos el compass con el STABLE,
volvemos a conectar la cluster pero ahora mediante COMPASS. copiamos la ruta. IMPORTANTE, debemos tener abierto el COMPASS,
y nos debe salir una ventana diciendo que si queremos establecer la conexion, damos si, y ponemos la contraseña, y agregamos un 
FAVORITE NAME, damos CONECTAr, Y EN COMPASS, veremos al lado izquierdo el panel con la conexion que nombramos en FAVORITE NAME:
la abrimos y veremos la BD y las colecciones que tengamos.

NOTA IMPORTANTE: No podemos usar SESSION como propiedades en una clase porque no tenemos la KEY COOKIES. Pero si en un metodo,
ya que solamente lo usamos cuando llamamos al metodo.
Si no le ponemos la KEY COOKIE no nos hara las cookies y como consecuenca no habra cookies ni SESSION.


"""