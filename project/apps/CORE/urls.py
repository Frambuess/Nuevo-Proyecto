from django.urls import path
from . import views
from .views import home, crear_clientes

app_name = "Home"

urlpatterns = [
 #   path('', views.index),
    path("", home, name="home"),
    path("clientes/", views.clientes, name="clientes"),
    path('crear_clientes/', crear_clientes, name="crear_clientes"),
]
