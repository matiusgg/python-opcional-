from django.shortcuts import render
# from  django.http import HttpResponse
#* Ahora para usar con RENDER
from django.shortcuts import render
from datetime import datetime
# Create your views here.

#* Lista que incluiremos dentro de la vista
posts = [
    {
        'name': 'Pepe',
        'user': 'P',
        'timestamp': datetime.now().strftime('%d/%m/%Y - %H:%Mh'),
        'picture': 'https://picsum.photos/id/37/200/300'
    }
]

def vistaApp(request):

    # content = []

    # for post in posts:

    #     content.append("""
    #     <p><strong> {name}</strong></p>
    #     <p><small> {user} - <i> {timestamp} </i></small></p>
    #     <figure> <img src="{picture}"/></figure>""".format(**post))


    # grupito = [3,5,6,7,7]

    # return HttpResponse(str(grupito))
    # return HttpResponse('<br>'.join(content))
    #* POSTS es la lista que hemos creado y que la hemos colcoado en un diccionario con los {}
    return render(request, 'feed.html', {'posts':posts})
