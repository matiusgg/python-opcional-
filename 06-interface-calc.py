from tkinter import *
from tkinter import messagebox

raiz = Tk()

raiz.title('CALCULADORA')

#*Variable global que almacenara la operacion
operacion = ''
resultado = 0
#*Variable global que nos permitira condicional en la funcion total() para decirle cual operaicon hacer.
operador = ''
primera_vez = False

#* Funcion que nos permitira nos
#*StringVar() nos permite convertir una variable a string
pulsarCero = StringVar()

def codigoBoton(num):
    #*Recuperamos la variable OPERACION con global que estaba afuera de la funcion.
    global operacion

    #* sI OPERACION NO ESTA VACIO, en el caso de que no opriman algun boton de numero, hazme esto:
    if operacion != '':

        #* Enviamos al VISOR mediante el SET con el numero nuevo, ya sin tener ninguna concatenacion.
        pulsarCero.set(num)
        #* Vovlemos a redefinir opracion, porque queremos que vuelva al estado inicial que era ''. Es decir, lo
        #* Refrescamos.
        operacion = ''
    else:
        #* Lo que hacemos con GET es que lo que halla recopilado el pulsarCero, se sume con un nuevo valor de un nuevo boton
        #* SET: Hace que enviemos la informacion de nuevo al Visor, al TEXTVARIABLE para mostrar la concatenacion hecha.
        #* GET: REcopila la informacion
        pulsarCero.set(pulsarCero.get() + num)

    #* Si se oprime el boton de limpiar, nos lo dejara en 0, pero este 0 no se eliminara y se concatenara con el siguiente boton
    #* de numero, por lo cual aqui mismo le damos si es 0 limpiamelo cuando se oprima un nuevo numero
    if pulsarCero.get() == '0':

        pulsarCero.set('')


#*funcion Sumar(). EXPLICACION: Al no recuperar con GET() el valor del boton de sumar, el visor se refrescara, ya que no tiene
#* ninguna referencia o algo como SET para poder enviarle informacion de nuevo al VISOR.
def sumar(num):
    #* Llamamos a Operacion mediante global, no la ponemos en los parametros porque queremos que se almacene globalmente
    #* para usar su valor en otra funcion.
    global operacion
    global resultado
    global operador

    operador = 'sumar'

    #* Asignamos 'sumar' para que la funcion codigoBoton() funcione y haga su trabajo.
    operacion = 'sumar'

    #* Sumamos 
    resultado += float(num)
    print(f'resultado: {resultado}')
    print(f'num: {num}')

    #*Enviamos RESULTADO al visor mediante el SET()
    pulsarCero.set(resultado)

def restar(num):
    global operacion
    global resultado
    global operador

    # print(num)
    resultado += float(num)
    print(f'resultado: {resultado}')
    print(f'num: {num}')
    
    operador = 'restar'

    operacion = 'restar'

    #*
    pulsarCero.set(abs(resultado))
    #*Para que nos convierta resultado en un nuevo negativo
    resultado *= -1

def mult(num):

    global operacion
    global resultado
    global operador
    global primera_vez

    #* hacemos este condicional para que cuando vuelva hacer una multiplicacion por segunda vez
    #* no reinicie RESULTADO a 0 de nuevo
    if resultado == 0 and primera_vez == False:

        primera_vez = True
        resultado = 1

    resultado *= float(num)

    operacion = 'multiplicar'

    operador = 'multiplicar'

    pulsarCero.set(abs(resultado))

def dividir(num):

    global operacion
    global resultado
    global operador
    global primera_vez

    #* hacemos este condicional para que cuando vuelva hacer una multiplicacion por segunda vez
    #* no reinicie RESULTADO a 0 de nuevo
    if resultado == 0 and primera_vez == False:
        #* Igualamos resultado al num para que no nos haga como al multiplicar, osea que no nos divida por 0
        resultado = float(num)

    else:
        #*Si no es 0, hazme esto.
        resultado /= float(num)

    

    operacion = 'dividir'

    operador = 'dividir'

    pulsarCero.set(abs(resultado))

    


#* Funcion Limpiar Visor:
def Limpiar():
    global resultado
    global primera_vez

    resultado = 0
    #* Ponemos primera_vez, por si es multiplicar se vuelva a reiniciar y para que se aplique el condicional
    #* de la funcion mult()
    primera_vez == False
    #* Vaciamos el visor simplemente poniendo a 0
    pulsarCero.set(resultado)

#* Funcion IGUAL A/REsultado
def total():

    global resultado
    global operador
    global operacion



    #* El valor de RESULTADO sera toda la operacion hecha anteriormente a menos de que no le hallan dado a Limpiar().
    #* Y lo sumamos con pulsarCero que seria "=", y "=" no tiene ningun valor numerico por lo cual nos devolvera el
    #* final de todo.
    #* Pero aqui es suma pero no es igual a los *, o dividir u otro.
    # total = resultado + float(pulsarCero.get())
    #* Por lo cual haremos un condicional
    if operador == 'sumar':
        total = abs(resultado + float(pulsarCero.get()))
    if operador == 'restar':
        total = abs(resultado - float(pulsarCero.get()))
    if operador == 'multiplicar':
        total = abs(resultado * float(pulsarCero.get()))
    if operador == 'dividir':
        total = abs(resultado / float(pulsarCero.get()))


    #* Lo enviamos
    pulsarCero.set(total)

    #*Si quiero anular la operacion
    operacion = 0



#* FRAME, no le ponemos el tamaño porque nos molestara con los tamaños de los botones que le pongamos mas adelante
#* Lo ponemos en el boton con COMMAND para llamarla
miFrame = Frame(raiz, width=100, height=500)

miFrame.pack()

#************
#^ALERTA POPUP. Esto nos sirve para ahcer ventanas de error

# def popup():

#     msg = messagebox.showinfo('mensaje', 'nombre mensaje')

#**********************

#*VISOR:Lo que se va a introducir dentro de textVariable en la interfaz sera pulsarCero que tiene el StringVar
#* Cuando pulsan algun boton, el textVariable permite mostrar el contenido del boton
visor = Entry(miFrame, textvariable=pulsarCero)
#*COLUMNSPAN: Nos permite posicionar el elemento entre columnas, es decir, no se quede en un celda
#*sino que se posiciones entre las columnas.
visor.grid(row=0, column=0, columnspan=4)
visor.config(bg='#2B2A33', fg='white', justify='center', width=25, font=('Verdana', 10))


#*************************

#BOTON1
#*En el command le decimos que ejecute la funcion, por lo cual al darle al boton, se ejecute, la cual esta tiene en su
#* interior el "pulsarCero" que tiene en el SET el "0". Este 0 se asigna al pulsarCero, y se mmuestra en el VISOR, ya que le
#* colocamos el pulsarCero en el "textVariable"
#* Aseguarte que las propiedades que les vas colocando al config en un elemento/objeto del FRAME, los demas elementos tambien tengan
#* esos mismos comandos en el config, es decir, que si por ejemplo en el config de un text() ponemos width y height, en otros elementos como
#* label, botones,textarea, etc. Segun lo que quieras, tengan estos mismas propiedades para que el CONFIG de cada unno identifique y los alinee.

botonUno = Button(miFrame, text='1', command=lambda:codigoBoton('1'))
botonUno.grid(row=2, column=0)
botonUno.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#****************************


#BOTON2
botonDos = Button(miFrame, text='2', command=lambda:codigoBoton('2'))
botonDos.grid(row=2, column=1)
botonDos.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************

#BOTON3
botonTres = Button(miFrame, text='3', command=lambda:codigoBoton('3'))
botonTres.grid(row=2, column=2)
botonTres.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************


#BOTON4
botoncuatro = Button(miFrame, text='4',command=lambda:codigoBoton('4'))
botoncuatro.grid(row=3, column=0)
botoncuatro.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************


#BOTON5
botonCinco = Button(miFrame, text='5', command=lambda:codigoBoton('5'))
botonCinco.grid(row=3, column=1)
botonCinco.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************


#BOTON6
botonSeis = Button(miFrame, text='6', command=lambda:codigoBoton('6'))
botonSeis.grid(row=3, column=2)
botonSeis.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************


#BOTON7
botonSiete = Button(miFrame, text='7', command=lambda:codigoBoton('7'))
botonSiete.grid(row=4, column=0)
botonSiete.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************


#BOTON8
botonOcho = Button(miFrame, text='8', command=lambda:codigoBoton('8'))
botonOcho.grid(row=4, column=1)
botonOcho.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************


#BOTON9
botonNueve = Button(miFrame, text='9', command=lambda:codigoBoton('9'))
botonNueve.grid(row=4, column=2)
botonNueve.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************

#*BOTON0
botonCero = Button(miFrame, text='0', command=lambda:codigoBoton('0'))
botonCero.grid(row=5, column=0, columnspan=2)
botonCero.config(width=14, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#*****************************

#*BOTON AC
botonCero = Button(miFrame, text='AC', command=lambda:Limpiar())
botonCero.grid(row=1, column=0)
botonCero.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))


#********************************************************

#*BOTON +/-
botonCero = Button(miFrame, text='+/-', command=lambda:codigoBoton('h'))
botonCero.grid(row=1, column=1)
botonCero.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))


#********************************************************

#*BOTON %
botonCero = Button(miFrame, text='%', command=lambda:codigoBoton('%'))
botonCero.grid(row=1, column=2)
botonCero.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid', font=('Arial', 15))

#FF8A08
#********************************************************

#********************************************************

#*BOTON ÷
botonCero = Button(miFrame, text='÷', command=lambda:dividir(pulsarCero.get()))
botonCero.grid(row=1, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid', font=('Arial', 15))


#********************************************************

#*BOTON x
botonCero = Button(miFrame, text='x', command=lambda:mult(pulsarCero.get()))
botonCero.grid(row=2, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid', font=('Arial', 15))



#********************************************************

#*BOTON -
botonCero = Button(miFrame, text='-', command=lambda:restar(pulsarCero.get()))
botonCero.grid(row=3, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid', font=('Arial', 15))



#********************************************************

#*BOTON +
#* VEMos que en el COMMAND llamamos a la funcion SUMAR y en su parametro ponemos la informacion
#* que se envia cuando le damos a algun boton de numero recuperandolo mediante GET
botonCero = Button(miFrame, text='+', command=lambda:sumar(pulsarCero.get()))
botonCero.grid(row=4, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid', font=('Arial', 15))

#********************************************************

#*BOTON =
botonCero = Button(miFrame, text='=', command=lambda:total())
botonCero.grid(row=5, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid', font=('Arial', 15))


#********************************************************


raiz.mainloop()