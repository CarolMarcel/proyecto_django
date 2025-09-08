# Importamos la función 'path' para definir rutas y 'views' para enlazarlas con nuestras vistas
from django.urls import path
from . import views

# Aquí se definen todas las rutas (URLs) de la aplicación "portafolio"
urlpatterns = [
     # Ruta principal ("/"), se conecta con la vista 'home'
    path('', views.home, name='home'),
    # Ruta "/contacto/", se conecta con la vista 'contacto'
    path('contacto/', views.contacto, name='contacto'),
    # Ruta "/gracias/", se conecta con la vista 'gracias'
    path('gracias/', views.gracias, name='gracias'),
    # Ruta "/theme/<modo>/", permite cambiar el tema (light, dark o auto)
    path("theme/<str:mode>/", views.set_theme, name="set_theme"),
]