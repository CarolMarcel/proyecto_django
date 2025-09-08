"""from django.shortcuts import render"""
# Importamos funciones de Django para manejar vistas
# Importamos el formulario que definimos en forms.py
from django.shortcuts import render, redirect
from .forms import ContactForm

# Vista principal (home): muestra la página inicial con la plantilla "home.html"
def home(request):
    return render(request, "portafolio/home.html")

# Vista de contacto:
# - Si el usuario envía el formulario (POST), valida los datos con ContactForm.
# - Si es válido, se podría guardar en la base de datos o enviar un correo.
# - Luego redirige a la página de "gracias".
# - Si el método es GET, solo muestra el formulario vacío.
def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # aquí guardar en BD o enviar correo
            return redirect("gracias")
    else:
        form = ContactForm()
    return render(request, "portafolio/contacto.html", {"form": form})

# Vista de agradecimiento:
# Se muestra después de enviar el formulario correctamente.
def gracias(request):
    return render(request, "portafolio/gracias.html")

# Vista para cambiar el tema (claro/oscuro/auto):
# No usa JavaScript, guarda la elección en una cookie.
# - "light" → fuerza modo claro
# - "dark"  → fuerza modo oscuro
# - "auto"  → elimina cookie y usa el tema según configuración del sistema
def set_theme(request, mode):
    """
    mode: 'light' | 'dark' | 'auto'
    - 'light' / 'dark' -> fija cookie 'theme'
    - 'auto'           -> elimina cookie (usa el tema del sistema)
    """
    if mode not in ("light", "dark", "auto"):
        mode = "auto"

    # Detecta a dónde debe volver el usuario después de cambiar el tema
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"

    resp = redirect(next_url)

    # Guardar o borrar cookie según la opción elegida
    if mode == "auto":
        resp.delete_cookie("theme")
    else:
        resp.set_cookie(
            "theme",
            mode,
            max_age=60 * 60 * 24 * 365,  # Duración 1 año
            samesite="Lax",      # seguridad básica de la cookie
        )
    return resp