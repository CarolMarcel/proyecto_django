from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["nombre", "email", "mensaje"]
        labels = {
            "nombre": "Nombre completo",
            "email": "Correo electrónico",
            "mensaje": "Mensaje",
        }
        widgets = {
            "mensaje": forms.Textarea(attrs={"rows": 4}),
        }

    