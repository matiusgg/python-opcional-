'''
ENTRY, es otro widge que actua como objeto dentro del FRAMe
'''
from tkinter import *

raiz = Tk()
#*PADx/y: Padding
miFrame = Frame(raiz, width=1000, height=500, padx=20, pady=20)
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

raiz.mainloop()