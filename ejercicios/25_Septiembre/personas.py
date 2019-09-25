
# * PRINCIPIO DE SUSTITUCION: ES a siempre b?. ES DECIR, LA subclase EMPLEADO ES SIEMPRE PERSONA? CLARO,
# * PERSONA ES SIEMPRE EMPLEADO? No porque es la superclase. Entonces es importante tener claro que si hacemos
# *ya qyue viene bien cuando tenemos muchas herencias, tener claro cuando son


class Persona():

    def __init__(self, nombre, edad, localidad):

        self.nombre = nombre
        self.edad = edad
        self.localidad = localidad

    def descripcion(self):

        print(
            f'Nombre: {self.nombre}, \n Edad: {self.edad}, \n Localidad: {self.localidad}')


# Subclases
# * Si tenemos un monton de herencias

class Empleado(Persona):

    # * Si hacemos un constructor en la subclase pisara el constructor de la superclase
    # * Para ello usamos como en JAVA, el SUPER

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, localidad_empleado):

        # * Como vemos en los parametros del super no es el mismo nombre de los atributos
        # * que de la superclase persona, esto es porque no va de nombre sino de la posicion de los
        # * parametros en la estructura del constructor del superclase.
        # * aDEMAS SI PONEMOS LOS MISMOS NOMBRES DE LOS ATRIBUTOS DEL CONSTRUCTOR DE SUPER
        # * COMO ORIGINALMENTE ESTABAN, TENDRIAMOS PROBLEMAS PORQUE LA SUBCLASE PISARIA LOS ATRIBUTOS
        # * PORQUE ESTAMOS VOLVIENDO A PONER EL MISMO NOMBRE DE LOS ATRIBUTOS DEL SUPER
        # * ESTOS NOMBRES YA SERIAN DE LA SUBCLASE
        super().__init__(nombre_empleado, edad_empleado, localidad_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()

        print(f'Salario: {self.salario}, \n Antiguedad: {self.antiguedad}')


Katy = Empleado(1800, 8, 'Katiana', 43, 'Rusa')

Katy.descripcion()

# * PARA COMPROBAR EL PRINCIPIO DE SUSTICION, PARA SABER QUE OBJETO PERTENECE A CUAL CLASE
# * DONMDE PODEMOS COMPROBAR SI EL OBJETO ES CREADO A PARTIR DE LA SUBCLASE, LA CUAL TAMBIEN TIENE
# * LA HERENCIA DE LA SUPERCLASE COMO SABEMOS, en donde podemos usar:
# * ISINSTANCE: Nos permite comprobar cual es la clase de un objeto y a su vez comprobar
# * si el objeto creado es a partir tambien de una superclase.
# * La cuestion aqui es que "katy" en este ejemplo es de EMPLEADO, por lo cual nos dara true
# * A su vez si ponemos PERSONA tambien nos dara TRUE porque EMPLEADO hereda de PERSONAS,
# * en cambio, si ponemos otra subclase u otra superclase que no conforma parte del objeto
# * nos dara error obviamente porque no fueron creados a partir de una clase y no de otra subclase u otra
# * superclase

print(isinstance(Katy, Persona))
