from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

# Create your views here.
from .models import Cliente, Mediodepago, Pais

def home(request):
    return render(request, "CORE/base.html")

def clientes(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "CORE/clientes.html", contexto)