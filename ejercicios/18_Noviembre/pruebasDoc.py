'''
PRUEBAS CON LA DOCUMENTACION
Saber que lo que programas fucniona adecuadamente antes de lanzarto a produccion o
antes de arrancarlo. Esto para ver como lo veria alguien mas.
'''

#* Creamos una funciond ejemplo
def areaTriangulo(base, altura):

    #* Como lo vamos a gestionar en documentacion?
    #* Usamos ">>>" que nos permite hacer pruebas de documentaicon la funcion por ejemplo,
    #* para decrile a la persona que lo lea lo que hara esta funcion
    #* la funcion en este caso. Para que nos sirve esto?. Esto nos beneficia para
    #* verificar si la funcion funciona adecuadamente. Si en la prueba lo que pongamos es correcto.
    #* No nos mostrara nada, pero si esta incorrecto nos mostrara los detalles del error de la prueba con ">>>".
    #* En este caso ahcemos una prueba para ver si la funcion verifica la informacion donde:
    #* llamamos a la funcion para ejecutarla, y una linea mas abajo ponemos el resutladfo que creemos que saldra.
    #* Por lo cual si el resultado que pusimos no es corrrecto o exacto. Nos mostrara el error.
    #* Resumidamente, podemos probar nuestras funciones sin necesidad de ir incluyendo print's por todas partes o inputs innecsarios para pruebas.
    """
    Calculando el area de un triangulo
    >>> areaTriangulo(3,3)
    4.0

    """


    return 'El resultado del triangulo es: ' + str((base * altura) / 2)

#* DOCTEST: ES una libreria que nos permite gestionar de mejor manera la documentacion.
#* Con DOCTEST no necesitamos llamar a la funcion en este caso porque la documentacion lo hace por nosotros.
import doctest
#* Nos abre una ventana en la terminal mas detallada.
doctest.testmod()
