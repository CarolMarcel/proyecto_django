from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('gracias/', views.gracias, name='gracias'),
    path("theme/<str:mode>/", views.set_theme, name="set_theme"),
]