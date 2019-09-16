
'''
AGENDA:

----------------

nombre/ telefono / email

'''

# CSV: Son archivos planos en donde hay datos simples separados por ",". o en nuestros caso lo haremos de esta forma.
# importamos la funcion de CSV
# TODOS los sistemas de datos tiene archivos XML, CSV y TXT.

import csv

class Ficha():

    def __init__(self, nombre, telefono, email):

        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda():

    # Constructor

    def __init__(self):

        self._contactos = []

    
    # Metodos

    # Añadir contacto:

    def anyadir(self, nombre, telefono, email):

        # Como lo hizo el profe con una lista no con diccionario como yo:

        # creo un objeto de la clase FICHA dentro de la clase Agenda, esto para usar
        # los atributos como valores

        contacto = Ficha(nombre, telefono, email)

        self._contactos.append(contacto)

                # COLOCAMOS el metodo _guardar() porque lo que queremos como en anyadir(), es que cada vez que borramos el contacto, 
        # que pise la informacion. ya que la funcion tiene "W" en el OPEN(), porque queremos que lo pise?. Porque nos beneficia,
        # al momento de recopilar informacion para no aumentar la memoria, ya que si usamos "a", si ira guardando lo anterior y
        # tendremos mas memoria. Ademas de que al momento de buscar no tengamos que ir uno por uno.

        self._guardar()

        print('Se ha añadido el contacto')

    # Mostrar todos los contacto

    def mostrar_todo(self):
        for contacto in self._contactos:

            self._mostrar(contacto)

    # mostrar contacto, es privado

    def _mostrar(self, contacto):

        print('-----*---------------*---------------*_--------------------*')
        print(f'Nombre: {contacto.nombre}')
        print(f'Telefono: {contacto.telefono}')
        print(f'Email: {contacto.email}')
        print('---------*--------------*-------------*------------------------*')


    def borrar(self, nombre):

        #ENUMERATE: Nos permite recoger los datos o valores de la posicion que ocupa ese valor o dato

        # COLOCAMOS el metodo _guardar() porque lo que queremos como en anyadir(), es que cada vez que borramos el contacto, 
        # que pise la informacion. ya que la funcion tiene "W" en el OPEN(), porque queremos que lo pise?. Porque nos beneficia,
        # al momento de recopilar informacion para no aumentar la memoria, ya que si usamos "a", si ira guardando lo anterior y
        # tendremos mas memoria. Ademas de que al momento de buscar no tengamos que ir uno por uno.

        for index, contacto in enumerate(self._contactos):

            if contacto.nombre.lower() == nombre.lower():

                # DEL: BOrrar el valor de una lista

                del self._contactos[index]

                self._guardar()

                print('Se ha borrado el contacto')

                # ponemos el break para que pare el for inmediatamente

                break

    def buscar(self, nombre):

        for contacto in self._contactos:

            if contacto.nombre.lower() == nombre.lower():

                self._mostrar(contacto)

                break
        

         # PODEMOS PONERLE ELSE AL FOR: COMO? Tenemos que tener en cuenta que el FOR debe tener condicionakes oara que funciones
         # porque hariamos esto, para que nos pare el bucle

        else:
            self._no_encontrado()


    def actualizar(self, nombre, telefono, email):

        for contacto in self._contactos:

            if contacto.nombre.lower() == nombre.lower():

                contacto.nombre = nombre
                contacto.telefono = telefono
                contacto.email = email

                print('Se ha actualizado correctamente')

                break
            
        else:
            self._no_encontrado()

    

    def _no_encontrado(self):

        print('*******')
        print('No encontrado')
        print('*******')

    def _guardar(self):

        with open('contactos.csv', 'w') as f:

            # WRITE: es una funcion de CSV para escribir
            escribir = csv.writer(f)

            # WRITEROW: Comunmente el archivo CSV, tiene en la priemra linea deifnido cuales columnas tendran datos en ellos
            # en este caso el WRITEROW permite que creeemos estas columnas ara despues con el for de la lista de contactos podamos 
            # introducirlos dentro de las columnas mediante el WRITEROW

            escribir.writerow( ('nombre', 'telefono', 'email'))

            for contacto in self._contactos:

                escribir.writerow( (contacto.nombre, contacto.telefono, contacto.email) )

    
    def salir(self):

        print('Haz salido de la agenda de contactos')


    # def __init__(self, nombre, telefono, email):

    #     self.nombre = nombre
    #     self.telefono = telefono
    #     self.email = email




# OBJETOS:
# Nos interesa empezar con  con CSV

def run():

        # Creamos un objeto para poder usarlo en el while y los condicionales

    agenda_matius = Agenda()

    # Lectura del archivo donde se almacena

    with open('contactos.csv', 'r') as f:

        #READER: es una funcion del csv

        leer = csv.reader(f)

        # 

        for index, row in enumerate(leer):

            if index == 0:

                continue

            else:

            # Lo que hacemosa es añadir un nuevo contacto mediante el artchivo CSV, en donde row son los datos del contacto
            # donde obviamente [0] es nombre, [1] es telefono y [2] es email, pero si fueran muchisimos, simplemente hariamos un for
            # para que vaya anclando o anyadiendo en este caso cada vez que haga una vuelta en el bucle, pero ya seria otro caso.
                agenda_matius.anyadir(row[0], row[1], row[2])

    # contactos = {}

    while True:

        print('''

        Que deseas hacer?
        [a]ñadir contacto
        [ac]tualizar
        [b]uscar contacto
        [e]liminar contacto
        [l]ista contactos
        [s]alir
        ''')

        menu = input('Escoge una opcion: ')


        if menu == 'a':
            
            nombre = input(' Introduce nombre: ')

            telefono = int(input(' Introduce el telefono: '))

            email = input(' Introduce el email: ')

            agenda_matius.anyadir(nombre, telefono, email)

            # contactos[nombre] = [telefono, email]

            # print(contactos)

            




        elif menu == 'ac':

            # print(contactos)
            # actualizar = input('Escoge cual contacto quieres actualizar: ')

            # for llave, valor in contactos.items():

                # if actualizar == llave:

            nombre = input(' Introduce nombre: ')

            telefono = int(input(' Introduce el telefono: '))

            email = input(' Introduce el email: ')

            agenda_matius.actualizar(nombre, telefono, email)



            # contactos[llave] = [telefono, email]

            # print(contactos)



        elif menu == 'b':




            buscar = input('Busca el contacto: ')


            agenda_matius.buscar(buscar)

    

            # for llave, valor in contactos.items():

            #     if buscar == llave:

            #         print(contactos)




        elif menu == 'e':

            eliminar = input('Escribe el contacto, para eliminarlo: ')

            agenda_matius.borrar(eliminar)      

        elif menu == 'l':

            agenda_matius.mostrar_todo()
                
        
        elif menu == 's':

            f.close()
            break
        
        else:

            print('Prueba Otra vez')

if __name__ == "__main__":
    run()

