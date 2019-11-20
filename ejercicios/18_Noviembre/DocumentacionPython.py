'''
DOCUMENTACION DE UN PROYECTO.
'''

#*Para documentar fucniones, clases, ... Se debe mantener en lo siguiente:
#*La documentacion sirve para los grupos de trabajo. respecto a la organizacion del proyecto
#*para documentar todo respecto al proyecto.
#* Ejemplo con varias funciones
def calcular():
	'Calcula tu edad con un solo parametro'
	pass
def calcularPeso():
	'cALCULA TU PESO'
	pass

# Pero ahora como sabemos si la documentacion fue correcta o si se agrego la documentacion?:
#* Usamos __doc__ para imprimirlo y verificarlo.
print(calcular.__doc__)

# HELP: Nos permite ver la documentacion de una forma de nota, en donde nos dara toda la
# informacion que nos esta pidiendo mas detallada.
help(calcular)

#* Si añadimos una clase con sus metodos. Podemos hacer dos cosas, solo documentar
#* los metodos o documentar la clase. Ejm:

class Calculos():
	
	""" Esta clase tiene dos metodos """
	
	def calcular():
	    'Calcula tu edad con un solo parametro'
	    pass
	def calcularPeso():
	    'cALCULA TU PESO'
	    pass

help(Calculos)
#* Si queremos ver un metodo especifico de esa clase.
help(Calculos.calcularPeso)

#* Para documentar tenemos que usar """.