from django.urls import path
from . import views
from .views import home

app_name = "Core"

urlpatterns = [
 #   path('', views.index),
    path("", home, name="Core"),
]
