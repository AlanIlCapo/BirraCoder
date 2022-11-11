from django.shortcuts import render, redirect
from .models import Cerveza
from django.http import HttpResponse
from .models import Menu, Cliente


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

    lista = Cerveza.objects.all()

    return render(request,"cervezas.html", {"cerveza":lista})  #"lista_cerveza.html", {"lista_cerveza":lista} )


def menu(request):

    lista = Menu.objects.all()

    return render(request, "menu.html", {"menu":lista})


def cliente(request):

    lista = Cliente.objets.all()

    return render(request, "cliente.html", {"cliente":lista})

#Formularios--------------------
def cervezaFormulario(request):

    if request.method=='POST':

        cerveza = Cerveza(estilo=request.POST['estilo'], ibu=request.POST['ibu'], alcohol=request.POST['alcohol'])
        cerveza.save()

        return redirect('Cervezas')
    
    else:
        return render(request, "cervezaFormulario.html")
    

def menuFormulario(request):

    if request.method=='POST':

        menu= Menu(minutas=request.POST['minutas'], descripcion=request.POST['descripcion'], precio=request.POST['precio'])
        menu.save()

        return redirect('Menu')
    
    else:
        return render(request, "menuFormulario.html")


def clienteFormulario(request):

    if request.method=='POST':

        menu= Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        menu.save()

        return redirect('Cliente')
    
    else:
        return render(request, "clienteFormulario.html")
