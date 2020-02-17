"""
URLS.py
"""

from django.urls import path
from pruebaDjango import views as local_views
from posts import views as post_views

urlpatterns = [
    path('hola/', local_views.hola_mundo),
    path('siguiente/', local_views.siguiente),
    #* Estamos convirtiendo datos que ponemos en la URL
    path('argumentos/<str:nombre>/<int:edad>', local_views.argumentos),
    #* ruta para la vista de la app que hemos creados.
    path('vistaApp/', post_views.vistaApp),

]
