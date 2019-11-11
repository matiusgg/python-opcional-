import pymysql

class Bd():

    def __init__(self, localhost, usuario, password, basedeDatos):

        self.conexion = pymysql.connect(localhost, user=usuario, password=password, db=basedeDatos)

    # Metodo de busqueda

    def query(self, sql):

        with self.conexion.cursor() as cursor:

            cursor.execute(sql)

            self.conexion.commit()

            self.conexion.close()

            return cursor.fetchall()