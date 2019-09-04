
'''
AGENDA:

----------------

nombre/ telefono / email

'''

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

        for index, contacto in enumerate(self._contactos):

            if contacto.nombre.lower() == nombre.lower():

                # DEL: BOrrar el valor de una lista

                del self._contactos[index]

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

    
    def salir(self):

        print('Haz salido de la agenda de contactos')


    # def __init__(self, nombre, telefono, email):

    #     self.nombre = nombre
    #     self.telefono = telefono
    #     self.email = email




# OBJETOS:

def run():

        # Creamos un objeto para poder usarlo en el while y los condicionales

    agenda_matius = Agenda()

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

            agenda_matius.salir() 
        
        else:

            print('Prueba Otra vez')

if __name__ == "__main__":
    run()

