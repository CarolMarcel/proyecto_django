from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, "portafolio/home.html")

def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # aquí podrías guardar en BD o enviar correo
            return redirect("gracias")
    else:
        form = ContactForm()
    return render(request, "portafolio/contacto.html", {"form": form})

def gracias(request):
    return render(request, "portafolio/gracias.html")