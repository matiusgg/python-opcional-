  
'''
EN EL CASO DE QUE LA CLASE CONSUMA MUCHO CONTENDIO DE LA CONEXION
ES MEJOR HACER DOS MODULOS, UNO CON LAS VARIABLES DE LA CONEXION Y OTRO
CON LA CLASE, Y EL MODULO DE CONEXION LO IMPORTAMOS DENTRO DEL MODULO DE LA CLASE
ESTO PARA TENERLO MAS CON MODULARIDAD Y QUE NO HALLAN ERRORES, estos en el mismo paquete
'''
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

        #* Lista solo 5 libros
        self.lista5Libros = []

    def Busqueda(self):

        #* ZONA SQL
        #****************************************

        sql = f'''
            SELECT a.name, b.title, b.price
            FROM books as b
            JOIN authors as a
            ON a.author_id = b.author_id
            WHERE b.title LIKE "{self.libro}%";
        '''
        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()
        
        if len(resultado) > 5:

            self.listaLibro.extend([resultado[0],resultado[1], resultado[2], resultado[3], resultado[4]])

            for i in self.listaLibro:

                self.lista5Libros.extend([i])

                print(self.lista5Libros)

            return self.lista5Libros


        else:
            
            for result in resultado:

                print(result)

                autor = result[0]
                libroAutor = result[1]
                precio = result[2]

                print(autor, libroAutor, precio)

                self.listaLibro.extend([[autor, libroAutor, precio]])

                print(self.listaLibro)

            return self.listaLibro


        # #* 4. Aceptar/Generar los QUERYS con:
        self.conexion.commit()

        #* 2. Cerrar la conexion
        self.conexion.close()

    def mostrarLibro(self):

        sql = f'''
            SELECT a.name, b.title, b.price
            FROM books as b
            JOIN authors as a
            ON a.author_id = b.author_id
            WHERE b.title LIKE "{self.libro}%";
        '''
        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

# usuario = input('Introduzca libro: ')

# obj = Libreria(usuario)
# obj.Busqueda()
