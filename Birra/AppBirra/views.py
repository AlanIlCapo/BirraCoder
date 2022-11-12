from django.shortcuts import render, redirect
from .models import Cerveza
from django.http import HttpResponse
from .models import Menu, Cliente
from .forms import CervezaFormulario, MenuFormulario, ClienteFormulario


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

def cliente (request, nombre, apellido, email):

    cliente = Cliente (nombre = nombre, apellido = apellido, email = email)

    cliente.save()

    return HttpResponse (f"""
    <p>nombre:{cliente.nombre} - apellido:{cliente.apellido} - email:{cliente.email} </p>
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

   

    if request.method =='POST':
        mi_formulario_cerveza = CervezaFormulario(request.POST)
        

        if mi_formulario_cerveza.is_valid():
            data = mi_formulario_cerveza.cleaned_data
            cerveza = Cerveza(estilo=data['estilo'], ibu=data['ibu'], alcohol=data['alcohol'])
            cerveza.save()
            return redirect('Cervezas')
    
    else:
        mi_formulario_cerveza = CervezaFormulario()

    return render(request, "cervezaFormulario.html", {'mi_formulario_cerveza': mi_formulario_cerveza})
    

def menuFormulario(request):
    mi_formulario_menu = MenuFormulario(request.POST)

    if mi_formulario_menu.is_valid():
        data = mi_formulario_menu.cleaned_data
        menu= Menu(minutas=data['minutas'], descripcion=data['descripcion'], precio=data['precio'])
        menu.save()
        return redirect('Menu')
    
    else:
        mi_formulario_menu = MenuFormulario()
    
    return render(request, "menuFormulario.html", {'mi_formulario_menu': mi_formulario_menu})


def clienteFormulario(request):
    mi_formulario_cliente = ClienteFormulario(request.POST)

    if  mi_formulario_cliente.is_valid():
        data = mi_formulario_cliente.cleaned_data
        cliente= Cliente(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
        menu.save()
        return redirect('Cliente')
    
    else:
        mi_formulario_cliente = ClienteFormulario()

    return render(request, "clienteFormulario.html", {'mi_formulario_cliente': mi_formulario_cliente})


def busqueda_cerveza(request):

    return render(request, 'busqueda_cerveza.html')

def buscar_cerveza(request):

    estilo_buscar = request.GET['estilo']

    cerveza = Cerveza.objects.get(estilo = estilo_buscar)

    return render(request, 'resultadoBusquedaEstilo.html', {'cerveza': cerveza, 'estilo':estilo_buscar})

