from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width= 999, height=490, padx=20, pady=20)

miFrame.pack()

#* NOMBRE
#**************************************

#*NombreLAbel para el ENTRY
nombreLable = Label(miFrame, text='Nombre: ')
#* Ahora en envez de enpaquetar el Label, vamos a usar GRID
# NombreLable.pack()
#*GRID:
#*STICKY: nos permite posicionar el contenido dentro de la celda que pusimos
#* en row y column., lo usamos con "n(norte), s(sur), "e(este), "w(oeste)"
nombreLable.grid(row=0, column=0, padx=5, pady=0, sticky='e')


#*ENTRY: Es un cuadro de texto, nos es un input
cuadroTexto = Entry(miFrame)
#*Enquetamos el ENTRY tambien dentro del FRAME
# cuadroTexto.pack()
#*Ahora usamos el GRID tambien en el ENTRY
cuadroTexto.grid(row=0, column=1, padx=0, pady=0)
#*Justify en este caso nos permite posicionar el texto dentro del ENTRY
cuadroTexto.config(fg='blue', justify='left')

#****************************************

#*emailLAbel para el ENTRY
emailLable = Label(miFrame, text='Email: ')
#* Ahora en envez de enpaquetar el Label, vamos a usar GRID
# emailLable.pack()
#*GRID:
emailLable.grid(row=1, column=0, padx=5, pady=0, sticky='e')

#*ENTRY: Es un cuadro de texto, nos es un input
emailTexto = Entry(miFrame)
#*Enquetamos el ENTRY tambien dentro del FRAME
#emailTexto.pack()
#*Ahora usamos el GRID tambien en el ENTRY
emailTexto.grid(row=1, column=1, padx=0, pady=0)
emailTexto.config(fg='blue', justify='left')

#*******************************************

#*passwordLAbel para el ENTRY
passwordLable = Label(miFrame, text='Contraseña: ')
#* Ahora en envez de enpaquetar el Label, vamos a usar GRID
# passwordLable.pack()
#*GRID:
passwordLable.grid(row=2, column=0, padx=5, pady=0, sticky='e')

#*ENTRY: Es un cuadro de texto, nos es un input
passwordTexto = Entry(miFrame)
#*Enquetamos el ENTRY tambien dentro del FRAME
#passwordTexto.pack()
#*Ahora usamos el GRID tambien en el ENTRY
passwordTexto.grid(row=2, column=1, padx=0, pady=0)
#*SHOW: Nos permite cambiar cambiar a que no se muetren los caractes.
passwordTexto.config(fg='blue', justify='center', show='*')

#*******************************************

#* COMENTARIOS

#*Generamos el label
comentariosLabel = Label(miFrame, text='Comentario: ')
comentariosLabel.grid(row=3, column=0, padx=5, pady=0, sticky='e')

#* Generamos el textarea
cuadroComentarios = Text(miFrame, width=30, height=5)
cuadroComentarios.grid(row=3, column=1, padx=0, pady=0)
cuadroComentarios.config(fg='grey', bd=1, relief='solid')

#* COMMAND: Nos permite ejecutar algo.
#*Scroll vertical para el textarea, donde en COMMAND le decimos que nos ejecute cuadroCommando y que lo junte
#* donde va estar el Scroll, y en que sentido se dirijira el Scroll en "yview"
#*en este caso verticalmente
scrollVert = Scrollbar(miFrame, command=cuadroComentarios.yview)
#*Ahora le vamos a decir que parte del grid estara el Scroll, "nsw(norte, sur, oeste)"
scrollVert.grid(row=3, column=2, sticky='nsw')
#*Ahora en la configuracion del textarea le ddecimos que adjunte el Scroll que creamos y mediante ".SET" lo fijamos en este.
cuadroComentarios.config(yscrollcommand=scrollVert.set)

#**************************************************************

#* BOTON

#* Vamos a crear una funcion para probar con el boton, lo que hara es que cuando le demos click al boton en la interfaz,
#* se ejecutara la funcion mediante el COMMAND.
def codigoBoton():
    pass

botonEnviar = Button(raiz, text='Enviar: ', command=codigoBoton)

#*Lo enpaquetamos en raiz
botonEnviar.pack()

#********************************************************
raiz.mainloop()