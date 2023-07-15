from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "CORE/index.html", {"saludo": "HOLAAA"})
