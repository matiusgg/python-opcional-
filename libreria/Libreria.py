  
import pymysql

class Libreria():

    def __init__(self, libro):

        self.libro = libro

        #* CONECTAR A BS MYSQL
        self.conexion = pymysql.connect('localhost', 'root', 'mysql', 'libreriatoni')


        #* 2. Crear cursor()
        self.cursor = self.conexion.cursor()

        #*ListaResultado

        self.listaLibro = []

    def Busqueda(self):

        #* ZONA SQL
        #****************************************

        sql = f'''
            SELECT a.name, b.title, b.price
            FROM books as b
            JOIN authors as a
            ON a.author_id = b.author_id
            WHERE b.title LIKE "{self.libro}";
        '''
        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

        for result in resultado:

            autor = result[0]
            libroAutor = result[1]
            precio = result[2]

            print(result, autor, libroAutor, precio)

            self.listaLibro.append(autor)
            self.listaLibro.append(libroAutor)
            self.listaLibro.append(precio)

            #****************************************

            return self.listaLibro

        # #* 4. Aceptar/Generar los QUERYS con:
        self.conexion.commit()

        #* 2. Cerrar la conexion
        self.conexion.close()
