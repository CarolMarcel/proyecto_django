
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portafolio.urls')),  # incluye las rutas de tu app
]
