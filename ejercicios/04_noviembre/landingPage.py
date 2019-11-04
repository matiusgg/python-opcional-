'''
LANDINGPAGE.
'''

#* ejercicio con flask en donde cada evz que le demos al boton cambia la imagen y el contenido cambia de color y texto segun la imagen
#* para ello vamos a usar la libreria DATETIME
import datetime
#* Fecha actual
mes = datetime.datetime.now()

print(mes.year)
#*%W: SEMANA(week), 0: domingo, 1:lunes, 2:martes, miercoles:3, etc.
print(mes.strftime('%w'))