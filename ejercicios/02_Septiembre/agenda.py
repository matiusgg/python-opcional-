
'''
AGENDA:

----------------

nombre/ telefono / email

'''

class Ficha:

    def __init__(self, nombre, telefono, email):

        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:

    # Constructor

    def __init_(self):

        self._contactos = []

    
    # Metodos

    # Añadir contacto:

    def anyadir(slef, nombre, telefono, email):

        # Como lo hizo el profe con una lista no con diccionario como yo:

        # creo un objeto de la clase FICHA dentro de la clase Agenda, esto para usar
        # los atributos como valores

        contacto = Ficha(nombre, telefono, email)

        self._contactos.append(contacto)

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


    def borrar(slef, nombre):

        #ENUMERATE: Nos permite recoger los datos o valores de la posicion que ocupa ese valor o dato

        for index, contacto in enumerate(self.contactos):

            if contacto.nombre.lower() == nombre.lower():

                # DEL: BOrrar el valor de una lista

                del self._contactos[index]

                break

    def buscar(self, name):

        for contacto in self._contacto:

            if contacto.nombre.lower() == nombre.lower():

                self._mostrae(contacto)

                break
        

         # PODEMOS PONERLE ELSE AL FOR: COMO? Tenemos que tener en cuenta que el FOR debe tener condicionakes oara que funciones
         # porque hariamos esto, para que nos pare el bucle

        else:
        self._no_encontrado()


    def actualizar(self, nombre, telefono, email):

        for contacto in self._contactos:

            if contacto.nombre.lower == name.lower():

                contacto.telefono = telefono
                contacto.email = email

                break
            
        else:
            self._no_encontrado()

    

    def _no_encontrado(self):

        print('*******')


    # def __init__(self, nombre, telefono, email):

    #     self.nombre = nombre
    #     self.telefono = telefono
    #     self.email = email




# OBJETOS:

def run():

        # Creamos un objeto para poder usarlo en el while y los condicionales

    agenda_matius = Agenda()

    contactos = {}

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

            contactos[nombre] = [telefono, email]

            print(contactos)

            




        elif menu == 'ac':

            print(contactos)
            actualizar = input('Escoge cual contacto quieres actualizar: ')

            for llave, valor in contactos.items():

                if actualizar == llave:

                    telefono = int(input(' Introduce el telefono: '))

                    email = input(' Introduce el email: ')

                    contactos[llave] = [telefono, email]

                    print(contactos)



        elif menu == 'b':
                
            buscar = input('Busca el contacto: ')

            for llave, valor in contactos.items():

                if buscar == llave:

                    print(contactos)


            # elif menu == 'e':
            #     pass

            # elif menu == 'l':
            #     pass
        
            # elif menu == 's':
            #     break
        
        else:

            print('Prueba Otra vez')

if __name__ == "__main__":
    run()

