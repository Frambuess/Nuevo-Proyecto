from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import ClienteForm

# Create your views here.
from .models import Cliente, Mediodepago, Pais

def home(request):
    return render(request, "CORE/base.html")

def clientes(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "CORE/clientes.html", contexto)

def crear_clientes(request):

    p1 = Pais(nombre="Argentina")
    p2 = Pais(nombre="Brasil")
    p3 = Pais(nombre="Uruguay")

    p1.save()
    p2.save()
    p3.save()

    m1 = Mediodepago(medio="Tarjeta de crédito Visa")
    m2 = Mediodepago(medio="Tarjeta de crédito Cabal")
    m3 = Mediodepago(medio="Tarjeta de crédito Master")

    m1.save()
    m2.save()
    m3.save()

    c1 = Cliente(pais_origen_id=p1, apellido="Ruiseñor", nombre="Almendra",
                 nacimiento=date(2015, 1, 1), medio_id=m1 , nrotarjeta="7666554486754544")
    c2 = Cliente(pais_origen_id=p2, apellido="Caras", nombre="Rosa",
                 nacimiento=date(2015, 1, 1), medio_id=m2 , nrotarjeta="7116554486754522")
    c3 = Cliente(pais_origen_id=p3, apellido="Juarez", nombre="Milena",
                 nacimiento=date(2015, 1, 1), medio_id=m3 , nrotarjeta="7666554486754566")
    c4 = Cliente(pais_origen_id=p1, apellido="Lopez", nombre="Pablo",
                 nacimiento=date(2015, 1, 1), medio_id=m1 , nrotarjeta="7666554486754588")

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    
    return redirect("Home:clientes")


def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home:clientes")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "CORE/crear.html", {"form": form})