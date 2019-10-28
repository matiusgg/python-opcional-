'''

LABEL es un widge, en las interfaces se encarganm de mucha scosas, ya sean traernos un texto, imagenes, etc. DEntro del main
no son iguales a los de HTML, el LABEL en si es un WIDGE, se coloca dentro del 
CREACION DE LABELS

'''

#*Inicializar/importar de nuevo Tkinter
from tkinter import *

#* Instancia/creacion de la clase TK
raiz=Tk()

#* Cremoas el FRAME
miFrame = Frame(raiz, width=500, height=400)
#* Y lo enpaquetamos dentro de la raiz tambien
miFrame.pack()

#*Creacion del LABEL
miLabel = Label(miFrame)
#* Y lo enpaquetamos dentro del FRAMe, pero
#*Si utilizamos el PACK dentro del FRAMe, las dimenciones se ajustan y se fijan dentro del lo que tenga el contenido
#* y eso no lo queremos porque no tendremos mas espacio para otras cosas
miLabel.pack()
#*Pero para solucionar esto usamos PLACE y le damos las dimenciones, esto sin tener que eliminar el miFrame(FRAME),
#*Ya que queremos mantener las dimenciones dadas en el FRAME.
miLabel.place(x=250, y=10)

#*forma de crear un LABEL de forma mas sencilla
Label(miFrame, text='Hola alumnos').place(x=250,y=10)

#*Opciones que tiene LABEL:
#*FG=darle color a la fuente
#*FONT= darle la tipografia y el tamaño
Label(miFrame, text='Hola alumnos',fg='red', font=('Arial',20)).place(x=250,y=10)

#*Crear LABEL->imagen
miImagen = PhotoImage(file='batman.gif')
Label(miFrame, image=miImagen).place(x=0,y=0)

raiz.mainloop()

