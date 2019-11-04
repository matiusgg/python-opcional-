from tkinter import *
#* Ventanas emergentes
from tkinter import messagebox
#* Abrir archivos
from tkinter import filedialog 


raiz = Tk()

#*Funcion de ventana Emergente
def ventanaEmergente():

    #* Ventana de informacion que ira integrada en algun subelemento, es decir, que cuando den click
    #* en algun subelemento nos abra esta ventana, donde
    #*SHOW(titulo de la ventana emergente, contenido)
    messagebox.showinfo('Calculadora 1.0', 'Calculadora 2019, desde muevete')

#* funcion Ventana de Licencia
def ventanaAvisoLicencia():

    #* ventana de warning
    messagebox.showwarning('Licencia', 'Licencia Libre para cualquier uso. No es posible comercializar con esta apliacion.')

#* funcion ventanaPregunta()
def ventanaPregunta():
    #*Ventana de opciones
    #*ASKQUESTION: Nos permite hacer una pregunta, pero ahora mismo no nos hace nada si no precionamos nada.
    # valor = messagebox.askquestion('Salir de la aplicacion', 'Quieres salir realmente')
    # #*Pero para que nos de un valor dependiendo de la respuesta, que seria en este caso YES, ya que  NO no nos haria nada.
    # if valor == 'yes':
    #     #*DESTROY nos cerraria la aplicacion
    #     raiz.destroy()

    #*Otra forma de hacerlo es mediante ASKOKCANCEL, que en vez de ser YES o NO, es CANCEL o OK
    valor = messagebox.askokcancel('Cerrar', 'Quieres salir realmente?')
    #* y nos viene bien ya que podemos usar TRUE or FALSE.
    if valor == True:
        raiz.destroy()


#*Funcion conectar
def conectar():

    #*ASKRETRYCANCEL, nos permite hacer una ventana de simulacion de conexion, en donde nos permitira dar a
    #* RETRY(intentar), nos aparecera el segundo parametro y si damos RETRY nos mostrara el primer parametro
    #* nos sirve si queremos conectar a una base de datos o aun servicio
    valor = messagebox.askretrycancel('Conectando...', 'Ha fallado la conexion')
    #* FALSE seria si le damos a CANCEL
    if valor == False:
        raiz.destroy()

#* Funcion abrir archivos
def abrirArchivos():

    #* PReguntamos la abertura de un archivo mediante el explorador de archivos
    #* INITIALDIR: ES donde le decimos la ruta predeterminada en el buscador
    #* FILETYPE: Es donde le decimos los tipos de archivos que podemos escoger. Hay que meterlo en tuplas, donde los elementos de la tupla seras minidesplegables/miniopciones
    #* para escoger entre tipos de archivos en el explorador de archivos
    archivo = filedialog.askopenfilename(title='Buscando archivo...', initialdir='~/Desktop', filetypes=(('Archivos de Excel', '*.xlsx'),
    ('Archivos de Texto', '*.txt'), ('Todos los archivos', '*.*')))
    
    #* Imprimir en terminal, lo que nos mostrara la ruta donde se encuantra ese archivo, esto nos beneficia para que podamos
    #*modificarlo, moldearlo a nuestro gusto.
    print(archivo)


#*  El menu se posiciona en la parte superior de la ventana
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

#* Cuantos elementos padre queremos en el menu. VEndrian a hacer los nombres principales de un menu que tendran dentro de ellos
#* sub-elementos que hacen partes de estos elementos principales.

#*menu. Aqui lo que hacemos es crear/instanciar un objeto de la clase Menu que etsa integrada en Tkinder
#* end donde como vemos estamos creando los elementos padre como por ejemlo, menu, edicion, herramientas y ayuda por ahora.
#* Tearoff: Nos permite eliminar un cuadro que sale en windows cuando damos click a un elemento, lo veras si quitas el tearoff
archivoMenu = Menu(barraMenu, tearoff=0)


#* SubElementos de archivoMenu
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Abrir...', command=abrirArchivos)

#*Ahora usaremos un "separador" de los subelementos, donde lo coloquemos nos separara el que esta debajo de los anteriores
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar', command=ventanaPregunta)
archivoMenu.add_command(label='Conectar', command=conectar)

#***********************************************************

archivoEdicion = Menu(barraMenu, tearoff=0)

#* SubElementos de archivoEdicion
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Pegar')
archivoEdicion.add_command(label='Editar')

#***********************************************************

archivoHerramientas = Menu(barraMenu, tearoff=0)

#* SubElementos de archivoHerramientas
archivoHerramientas.add_command(label='Formatear')


#***********************************************************

archivoAyuda = Menu(barraMenu, tearoff=0)

#*SubElementos de archivoAyuda
archivoAyuda.add_command(label='Acerca de...', command=ventanaEmergente)
archivoAyuda.add_command(label='Ver licencia', command=ventanaAvisoLicencia)

#***********************************************************

#* Hacer visible los elementos-padre en pantalla.
#*diferencia con LABEL: Si creamos un objeto con la clase Label, es con la L mayuscula/ si es una propiedad que va dentro de los ().
#* Se escribe obviamente con L minuscula.
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edicion', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)

#***********************************************************



raiz.mainloop()