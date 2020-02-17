#* para recibir una respuesta en http
from django.http import HttpResponse
import json

#* Vista de Hola Mundo
def hola_mundo(request):
    return HttpResponse('hola Mundo')

#* Vista de Siguiente
def siguiente(request):
    numeros = [int(i) for i in request.GET['numeros'].split(",")]
    ordenarnumeros = sorted(numeros)
    # import pdb; pdb.set_trace()

    #* Datos que enviaremos a un JSON
    datos = {
        'estado': 'valido',
        'numeros': ordenarnumeros,
        'mensaje': 'prueba test'
    }
    #* Retornar en el navegor en formato JSON
    #* DUMPS: Nos permite ajustar el contenido de un diccionario
    #* en JSON, Además para identar y que se vea más organizado usamos
    #* indent=numero de identación
    return HttpResponse(json.dumps(datos, indent=4), content_type='application/json')

    #* comprehensions de lista con números
#* Dentro de los parametros de la función argumentos
#* recogemos los parámetros que colocamos en la URL
def argumentos(request, nombre, edad):

    if edad < 18:
        mensaje = 'Eres menor de 18 años, vete pa tu casa'

    else:
        mensaje = f'bienvenido: {nombre}'

    return HttpResponse(mensaje)