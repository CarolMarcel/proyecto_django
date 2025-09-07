from django.db import models

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"

    def __str__(self):
        return f"{self.nombre} <{self.email}> ({self.creado:%Y-%m-%d %H:%M})"
