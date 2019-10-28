'''
INTERFACE GRAFICA PYTHON

CREACION DEL FRAME:
Copiamos lo mismo que teniamos en el anterior archivo 01-interface_raiz
'''

#*Inicializar/importar de nuevo Tkinter
from tkinter import *

#* Instancia/creacion de la clase TK
raiz=Tk()


#*Hay dos maneras de cerrar el mainloop, 1. Desde la consola, la cerramos o cerrando la interfaz

#*Titulo de la centana
raiz.title('Primera interface')

#*Contrlar el ancho y el alto de la ventana, con booleanos
#*Usamos RESIZABLE, funciona de siguiente manera: Funciona como si fuera cartesiano, pero en los (ancho, alto). Y "0" sigfinica
#* que no se puee modificar mientras que "1" podemos moficarlo.
#*Lo mas comun es que no se pueda modicar porque alteraria el contenido de la interfaz, es dependiendo de como se creo lainterfaz.
raiz.resizable(0,0)

#* Pero podemos definir el tamaño de la ventana
raiz.geometry('800x600')

#*Cambiar el icono que nos aparece en la ventana arriba
raiz.iconbitmap('python.ico')

#*diferentes configuraciones. CONFIG nos permitira realizar muchas opciones sobre la interface
#*"bg=color": nos permite colocar color de fondo a la interface.
raiz.config(bg='red')

#*DESDE AQUI ANTES DE MAINLOOP GENERAREMOS EL FRAME
'''FRAME'''
#*INSTANCIAR/CREAR la clase Frame
primerFrame= Frame()
#* Ahora necesitamos enpaquetar/meter dentro de la raiz, la clase frame dentro de la raiz, porque como ya se menciono, depsues de la raiz va el frame.
#*Ahora al enpaquetar el Frame, es como si raiz fuera el padre, y el FRAMe seria el hijo, ya que lo hemos metido/enpaquetado dentro de la raiz.
#* Por lo cual veremos podemos ir denfiniendo tambien propios tamaños, color, etc. con config
#* Con el codigo de ahora, veremos que la raiz es color rojo, y frame amarillo, ya que lo hemos colocado as y veremos
#* Como lo hicimos.
primerFrame.pack()

#*Color FRAMe
primerFrame.config(bg='yellow')

#* eliminamos el tamaño de la ventana en la raiz con nuestro nuevo tamaño del FRAME
primerFrame.config(width='500', height='400')

#* Creamso unos bordes al FRAMe, para que veamos ams la difenncia
primerFrame.config(bd=1)
#*Tipo de border
primerFrame.config(relief='groove')

#* Si nos interesa mover/posicionar el FRAMe alrededor de la raiz, Usamos PACK porque es el propio FRAMe es que queremos mover
#*SIDE: Nos lo permite mover horizontalmente, ACHOR, moverlo verticalmente. "s(sur)"
primerFrame.pack(side='right', anchor='s')

#*En el caso de que queramos moverlo mas exactamente, usamos el modo cartesiano, en FILL, decimos cual queremos modificar
#* Y EXPAND lo podemos expandir en ese eje
primerFrame.pack(fill='y', expand='True')

#*Cambiar el icono del cursor del raton
primerFrame.config(cursor='pirate')


#* Necesitamos crear un bucle infinito, para que la ventana en la cual este el usuario, este "escuchando" las peticiones
#* y acciones del usuario permanentemente
#* Nos abrira una ventana que seria la interfaz.
raiz.mainloop()

