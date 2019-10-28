from tkinter import *
from tkinter import messagebox

raiz = Tk()

#* Funcion que nos permitira nos
#*StringVar() nos permite convertir una variable a string
pulsarCero = StringVar()

def codigoBoton(num):

    #* Lo que hacemos con GET es que lo que halla recopilado el pulsarCero, se sume con un nuevo valor de un nuevo boton
    pulsarCero.set(pulsarCero.get() + num)

#* FRAME, no le ponemos el tamaño porque nos molestara con los tamaños de los botones que le pongamos mas adelante
#* Lo ponemos en el boton con COMMAND para llamarla
miFrame = Frame(raiz, width=100, height=500)

miFrame.pack()

#************
#^ALERTA POPUP. Esto nos sirve para ahcer ventanas de error

def popup():

    msg = messagebox.showinfo('mensaje', 'nombre mensaje')

#**********************

#*VISOR:Lo que se va a introducir dentro de textVariable en la interfaz sera pulsarCero que tiene el StringVar
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
botonUno.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#****************************


#BOTON2
botonDos = Button(miFrame, text='2', command=lambda:codigoBoton('2'))
botonDos.grid(row=2, column=1)
botonDos.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************

#BOTON3
botonTres = Button(miFrame, text='3', command=lambda:codigoBoton('3'))
botonTres.grid(row=2, column=2)
botonTres.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************


#BOTON4
botoncuatro = Button(miFrame, text='4',command=lambda:codigoBoton('4'))
botoncuatro.grid(row=3, column=0)
botoncuatro.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************


#BOTON5
botonCinco = Button(miFrame, text='5', command=lambda:codigoBoton('5'))
botonCinco.grid(row=3, column=1)
botonCinco.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************


#BOTON6
botonSeis = Button(miFrame, text='6', command=lambda:codigoBoton('6'))
botonSeis.grid(row=3, column=2)
botonSeis.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************


#BOTON7
botonSiete = Button(miFrame, text='7', command=lambda:codigoBoton('7'))
botonSiete.grid(row=4, column=0)
botonSiete.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************


#BOTON8
botonOcho = Button(miFrame, text='8', command=lambda:codigoBoton('8'))
botonOcho.grid(row=4, column=1)
botonOcho.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************


#BOTON9
botonNueve = Button(miFrame, text='9', command=lambda:codigoBoton('9'))
botonNueve.grid(row=4, column=2)
botonNueve.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************

#*BOTON0
botonCero = Button(miFrame, text='0', command=lambda:codigoBoton('0'))
botonCero.grid(row=5, column=0, columnspan=2)
botonCero.config(width=14, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#*****************************

#*BOTON AC
botonCero = Button(miFrame, text='AC', command=lambda:codigoBoton('AC'))
botonCero.grid(row=1, column=0)
botonCero.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')


#********************************************************

#*BOTON +/-
botonCero = Button(miFrame, text='+/-', command=lambda:codigoBoton('h'))
botonCero.grid(row=1, column=1)
botonCero.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')


#********************************************************

#*BOTON %
botonCero = Button(miFrame, text='%', command=lambda:codigoBoton('%'))
botonCero.grid(row=1, column=2)
botonCero.config(width=6, height=3, bg='#56585E', fg='white', bd=1, relief='solid')

#FF8A08
#********************************************************

#********************************************************

#*BOTON ÷
botonCero = Button(miFrame, text='÷', command=lambda:codigoBoton('÷'))
botonCero.grid(row=1, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid')


#********************************************************

#*BOTON x
botonCero = Button(miFrame, text='x', command=lambda:codigoBoton('x'))
botonCero.grid(row=2, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid')



#********************************************************

#*BOTON -
botonCero = Button(miFrame, text='-', command=lambda:codigoBoton('-'))
botonCero.grid(row=3, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid')



#********************************************************

#*BOTON +
botonCero = Button(miFrame, text='+', command=lambda:codigoBoton('+'))
botonCero.grid(row=4, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid')

#********************************************************

#*BOTON =
botonCero = Button(miFrame, text='=', command=lambda:codigoBoton('='))
botonCero.grid(row=5, column=3)
botonCero.config(width=6, height=3, bg='#FF8A08', fg='white', bd=1, relief='solid')


#********************************************************


raiz.mainloop()