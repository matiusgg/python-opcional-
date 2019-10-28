'''

INTERFACE GRAFICAS DE PYTHON
1. Creamos la raiz
2. Luego e FRAMe
3. Luego los widges que serain los objetos que conforman las interfaz

Para que nos abra como una interface, ponemos en el nombre del archivo "nombreInterface.pyw"

# Creamos la RAIZ



'''

#* INICIALIZAR libreria Tkinter, esta dentro de la biblioteac de python, no hay que hacer piip install
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


#* Necesitamos crear un bucle infinito, para que la ventana en la cual este el usuario, este "escuchando" las peticiones
#* y acciones del usuario permanentemente
#* Nos abrira una ventana que seria la interfaz, y si no lo ponemos no nos lo abrira.
raiz.mainloop()