from django.urls import path
from . import views
from .views import home, crear_cliente, busqueda

app_name = "Home"

urlpatterns = [
 #   path('', views.index),
    path("", home, name="home"),
    path("clientes/", views.clientes, name="clientes"),
    path('crear/', crear_cliente, name="crear"),
    path('busqueda/', busqueda, name="busqueda"),
]
