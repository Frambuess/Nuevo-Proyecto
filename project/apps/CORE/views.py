from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
#from django.urls import is_valid_path
from .forms import ClienteForm

# Create your views here.
from .models import Cliente, Mediodepago, Pais

def home(request):
    return render(request, "CORE/base.html")


def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home:clientes")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "CORE/crear.html", {"form": form})