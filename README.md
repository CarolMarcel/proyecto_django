# 🌐 Portafolio Django — Carol y Daniela

Proyecto de portafolio personal creado con **Django**, desplegado en **Railway**.  
El sitio incluye secciones de presentación, proyectos destacados y un formulario de contacto funcional.

---

## 📋 Características principales
- 🖼️ Página de inicio con presentación de integrantes (con foto, hobbies y estudios).
- 🎨 Diseño responsive con soporte de **modo claro / oscuro** (sin JavaScript, usando cookies).
- 🗂️ Sección de proyectos destacados.
- 📬 Formulario de contacto con validación de datos.
- 🚀 Despliegue en Railway listo para producción.

---

## ⚙️ Requisitos previos
Asegúrate de tener instalado en tu entorno:

- [Python 3.11+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Django 5.x](https://www.djangoproject.com/)
- Cuenta en [Railway](https://railway.app/)

---

Crear y activar entorno virtual:

python -m venv venv
venv\Scripts\activate #Windows
---
Instalar dependencias:

pip install -r requirements.txt
---
Ejecutar migraciones:

python manage.py migrate
---
Ejecutar migraciones:

python manage.py migrate    Luego abre http://127.0.0.1:8000
---
🌙 Temas (claro / oscuro)

El proyecto permite alternar entre:

☀️ Claro

🌙 Oscuro

🖥️ Automático (según el sistema)

Esto se logra mediante cookies sin necesidad de JavaScript:

# views.py
def set_theme(request, mode):
    ...
---
🚀 Despliegue en Railway

1. Sube tu código a GitHub.

2. Crea un nuevo proyecto en Railway vinculado al repositorio.

3. Configura las variables necesarias en Settings → Variables.

4. Railway construirá y desplegará automáticamente tu app.
---

👩‍💻 Autora

Carol Marcel

---

📄 Licencia

Este proyecto es de uso académico y libre para fines de aprendizaje.
---
