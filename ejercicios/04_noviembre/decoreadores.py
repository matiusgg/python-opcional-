'''
REPASO/EJEMPLO CON DECORADORES
#* Sirve para ayudar apliementar esas funciuonalidad que no tienen otras funciones.
#* en vez de ir a una funcion e implementarle el nuevo condigo, dando lugar a que se creen conflictos
#*ya que estamos interfiriendo directamente con el codigo de la funcion/funciones ya realizada, para eso estan los decoradores, para implementar
#*funcionalidades sin afectar al codigo previo de la funcion.
#* Ademas nos ahorra codigo porque con solo un decorador podemos agregarle a funcionalidades a  muchas funciones.
#* ya que nos ahorraremos en escribir el contenido del decorador en cada uno de ellos y nos tardartiamos mas y tendriamos mas codigo.
'''

#* Decorador
def funcionDecorador(funcionParametro):

    def funcionInterior():

        #* imprimir antes
        print('Estas apunto de ver un calculo')

        #* Regocemos la funcionParametro y la inicializamos, La funcion que va arecibir la decoracion
        #* se va a introducir a funcionParametro y con ello podemos usarlo aqui

        funcionParametro()


        #* Imprimir despues
        print('finalizado el calculo')
    
    #* Retorname la funcionalidad/contenido del decorador/(funcion que tiene el contenido de codigo) para agregarselo a las funciones que le hemos implentado el decorador.
    return funcionInterior

@funcionDecorador
def suma():
    print(5 + 5)

suma()