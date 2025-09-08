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

# --- Tema claro/oscuro sin JS: guarda elección en cookie ---
def set_theme(request, mode):
    """
    mode: 'light' | 'dark' | 'auto'
    - 'light' / 'dark' -> fija cookie 'theme'
    - 'auto'           -> elimina cookie (usa el tema del sistema)
    """
    if mode not in ("light", "dark", "auto"):
        mode = "auto"

    # Vuelve a donde estaba la persona (o al home)
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"

    resp = redirect(next_url)

    if mode == "auto":
        resp.delete_cookie("theme")
    else:
        resp.set_cookie(
            "theme",
            mode,
            max_age=60 * 60 * 24 * 365,  # 1 año
            samesite="Lax",
        )
    return resp