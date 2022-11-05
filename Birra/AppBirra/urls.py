
from django.urls import path
from .views import cerveza, menu, lista_cerveza, inicio, cervezas, cliente

urlpatterns = [
    path('cerveza/<estilo>/<ibu>/<alcohol>', cerveza),
    path('menu/<minutas>/<descripcion>/<precio>', menu),
    path('lista-cervezas/', lista_cerveza),
    path('', inicio),
    path('cervezas/', cervezas, name="Cervezas"),
    path('menu/', menu, name="Menu"),
    path('cliente/', cliente, name="Cliente"),
]
