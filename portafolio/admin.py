# Importa el panel de administración de Django 
from django.contrib import admin
# Importa el modelo ContactMessage desde models.py
from .models import ContactMessage

# Registra el modelo en el panel de administración de Django
# usando un decorador (@admin.register).
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Campos que se verán como columnas en la lista de mensajes
    list_display = ("nombre", "email", "creado")
    # Campos que serán de solo lectura en el detalle de un registro
    readonly_fields = ("creado",)

