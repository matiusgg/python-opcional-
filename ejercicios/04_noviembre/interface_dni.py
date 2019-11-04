from tkinter import *
#* Ventanas emergentes
from tkinter import messagebox
#* Abrir archivos
from tkinter import filedialog


raiz = Tk()

#*Titulo de la centana
raiz.title('Primera interface')

raiz.resizable(0,0)

#* Pero podemos definir el tamaño de la ventana
raiz.geometry('800x600')

#*Cambiar el icono que nos aparece en la ventana arriba
raiz.iconbitmap('python.ico')

#***************************************

#* funcion ventanaPregunta()
def ventanaPregunta():
    #*Ventana de opciones

    valor = messagebox.askokcancel('Cerrar', 'Quieres salir realmente?')

    if valor == True:
        raiz.destroy()

#***************************************

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)

#***************************************

archivoMenu.add_command(label='Cerrar', command=ventanaPregunta)

barraMenu.add_cascade(label='BuscarLogo', menu=archivoMenu)

# imagenFrame = Frame(raiz, width='100', height='50',padx=10, pady=10)
# imagenFrame.pack()
# imagenFrame.config(bg='yellow')


# #*Crear LABEL->imagen
# miImagen = PhotoImage(file='españa.png')
# labelEspanya = Label(imagenFrame, image=miImagen)
# labelEspanya.grid(row=0, column=0)
# labelEspanya.config(width='80', height='45')


# miFrame= Frame(raiz, padx=30, pady=30)
# miFrame.pack()
# miFrame.config(width='700', height='300', bg='red')

# #*Crear LABEL->imagen
# ImagenDni = PhotoImage(file='dni.png')
# labelImgDni = Label(miFrame, image=ImagenDni)
# labelImgDni.grid(row=0, column=0, padx=5, pady=5, rowspan=4)


# labelDni = Label(miFrame, text='Buscamos tu letra DNI:')

# labelDni.grid(row=0, column=1, padx=5, pady=0, sticky='e')


# #*ENTRY: Es un cuadro de texto, nos es un input
# cuadroTexto = Entry(miFrame)
# #*Enquetamos el ENTRY tambien dentro del FRAME
# # cuadroTexto.pack()
# #*Ahora usamos el GRID tambien en el ENTRY
# cuadroTexto.grid(row=1, column=1, padx=0, pady=0)
# #*Justify en este caso nos permite posicionar el texto dentro del ENTRY
# cuadroTexto.config(fg='blue', justify='left')

# botonUno = Button(miFrame, text='AVERIGUAR')
# botonUno.grid(row=2, column=1, padx=3, pady=3)

# raiz.mainloop()

'''
COMO LO HIZO EL PROFE

'''

#**************************************

#* zonaBuscar
zonaBuscar = StringVar()

def letraDni():
    letras = {0:'T',1:'R',2:'W',3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"}

    numeros = int(zonaBuscar.get())
    resto = numeros % 23

    letra = letras[resto]

    resultado.config(text=str(numeros) + '-' + letra)


#**************************************
#HEADER
frameHeader = Frame(raiz)
#*ANCHOR: El ancho hacia el norte "n"
frameHeader.pack(fill='x', anchor='n')
frameHeader.config(height='80')
#Header: Widgets
logo = PhotoImage(file='descarga.png')
Label(frameHeader, image=logo).pack()

#**************************************

FrameDni= Frame(raiz, padx=5, pady=10)
FrameDni.place(x=0, y=80)
FrameDni.config(width='400', height='200', padx=5, pady=20)

#**************************************

#*Crear LABEL->imagen
ImagenDni = PhotoImage(file='dni.png')
Label(FrameDni, image=ImagenDni).pack()


#**************************************

frameInput= Frame(raiz, padx=5, pady=10)
frameInput.place(x=410, y=80)
frameInput.config(width='400', height='200', padx=20, pady=50)

#*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?

labelDni = Label(frameInput, text='Buscamos tu letra DNI:', font=('Arial', 25))

labelDni.grid(row=0, column=0, columnspan=2)

#*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?


#*ENTRY: Es un cuadro de texto, nos es un input
cuadroTexto = Entry(frameInput, font=('Verdana', 14), textvariable=zonaBuscar)
#*Enquetamos el ENTRY tambien dentro del FRAME
# cuadroTexto.pack() 
#*Ahora usamos el GRID tambien en el ENTRY
cuadroTexto.grid(row=1, column=0, pady=40)


#*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?

botonUno = Button(frameInput, text='AVERIGUAR', command=letraDni)
botonUno.grid(row=1, column=1)

#*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?*?


resultado = Label(frameInput, font=('Arial', 40))
resultado.grid(row=2, column=0, columnspan=2)

#*************************************************************

framefooter = Frame(raiz)
framefooter.pack(fill='x', expand='True', anchor='s')
framefooter.config(height='60', bg='red')




raiz.mainloop()