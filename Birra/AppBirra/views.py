from django.shortcuts import render
from .models import Cerveza
from django.http import HttpResponse
from .models import Menu


def cerveza (request, estilo, ibu, alcohol):

    cerveza = Cerveza(estilo = estilo, ibu = ibu, alcohol = alcohol)

    cerveza.save()

    return HttpResponse (f"""
    <p>estilo:{cerveza.estilo} - ibu:{cerveza.ibu} -alcohol:{cerveza.alcohol} </p>
    """)


def menu (request, minutas, descripcion, precio):

    menu = Menu (minutas = minutas, descripcion = descripcion, precio = precio)

    menu.save()

    return HttpResponse (f"""
    <p>minutas:{menu.minutas} - descripcion:{menu.descripcion} -precio:{menu.precio} </p>
    """)

def lista_cerveza(request):

    lista = Cerveza.objects.all()

    return render(request, "lista_cerveza.html", {"lista_cerveza":lista})


def inicio(request):

    return render(request, "inicio.html")


def cervezas(request):

    return render(request, "cervezas.html")


def menu(request):

    return render(request, "menu.html")


def cliente(request):

    return render(request, "cliente.html")
