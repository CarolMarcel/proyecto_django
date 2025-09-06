from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=120, label="Nombre")
    email = forms.EmailField(label="Correo")
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"rows":4}), label="Mensaje")

    