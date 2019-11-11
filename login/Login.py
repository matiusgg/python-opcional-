from Conexion import Bd

class Login(Bd):

    def __init__(self, usuario, contrasenya, ):

        super().__init__(

    def logearse(self, sql):

        with self.conexion.cursor() as cursor:

            cursor.execute(sql)

            resultado = cursor.fetchall()

            for i in resultado:
                print(resultado)

            self.conexion.commit()

            self.conexion.close()

            return cursor.fetchall()

