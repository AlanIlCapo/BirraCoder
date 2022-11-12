
from django.urls import path
from .views import cerveza, menu, lista_cerveza, inicio, cervezas, cliente, cervezaFormulario, menuFormulario, clienteFormulario, busqueda_cerveza, buscar_cerveza

urlpatterns = [
    path('cerveza/<estilo>/<ibu>/<alcohol>', cerveza),
    path('menu/<minutas>/<descripcion>/<precio>', menu),
    path('cliente/<nombre>/<apellido>/<email>', cliente),
    path('lista-cervezas/', lista_cerveza),
    path('', inicio),
    path('cervezas/', cervezas, name="Cervezas"),
    path('menu/', menu, name="Menu"),
    path('cliente/', cliente, name="Cliente"),
    path('cervezaFormulario/', cervezaFormulario, name="cervezaFormulario"),
    path('menuFormulario/', menuFormulario, name="menuFormulario"), 
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('busqueda_cerveza/', busqueda_cerveza, name="busqueda_cerveza"),
    path('buscar_cerveza/', buscar_cerveza, name="buscar_cerveza"),
]
