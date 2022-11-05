
from django.urls import path
from .views import cerveza, menu, lista_cerveza, inicio, cervezas, cliente

urlpatterns = [
    path('cerveza/<estilo>/<ibu>/<alcohol>', cerveza),
    path('menu/<minutas>/<descripcion>/<precio>', menu),
    path('lista-cervezas/', lista_cerveza),
    path('', inicio),
    path('cervezas/', cervezas),
    path('menu/', menu),
    path('cliente/', cliente),
]
