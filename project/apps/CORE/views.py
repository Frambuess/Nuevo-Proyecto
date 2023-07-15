from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
#from django.urls import is_valid_path
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


def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home:clientes")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "CORE/crear.html", {"form": form})


def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "M"
    cliente_nombre = Cliente.objects.filter(nombre__contains="M")

    # Nacimientos  mayores a 2005
    cliente_nacimiento = Cliente.objects.filter(
        nacimiento__gt=date(2005, 1, 1))
    
    #today = date.today()
    #age = today.year - Cliente.nacimiento.year - ((today.month, today.day) < (Cliente.nacimiento.month, Cliente.nacimiento.day))

    # País de origen vacío
    cliente_pais = Cliente.objects.filter(pais_origen_id=None)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_nacimiento": cliente_nacimiento,
        "clientes_pais": cliente_pais
    }
    return render(request, "CORE/search.html", contexto)