"""
Archivo de configuración principal de Django para el proyecto "proyecto_django".
Contiene todos los ajustes de seguridad, aplicaciones instaladas,
configuración de base de datos, plantillas y archivos estáticos.
"""

from pathlib import Path
import os
import dj_database_url    # Para configurar base de datos en Railway
from decouple import config    # Para leer variables de entorno (SECRET_KEY, DEBUG, etc.)


# --- RUTAS BASE --- 
# Define la carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD ---
# Clave secreta (se obtiene de variables de entorno para mayor seguridad)
SECRET_KEY = config("SECRET_KEY", default="dev-insegura")

# Activa/desactiva el modo debug (en producción debe ser False)
DEBUG = config("DEBUG", default=True, cast=bool)

# Dominios permitidos (en Railway puede quedar abierto con "*")
ALLOWED_HOSTS = ["*"]  

# Dominios confiables para protección CSRF (necesario en Railway)
CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",
    "https://proyectodjango-production.up.railway.app",  # dominio exacto
]

# Seguridad adicional al trabajar detrás de proxy HTTPS (Railway)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# --- Applicaciones ---

INSTALLED_APPS = [
    'django.contrib.admin',   # Panel de administración
    'django.contrib.auth',     # Autenticación de usuarios
    'django.contrib.contenttypes',     # Manejo de tipos de contenido
    'django.contrib.sessions',    # Sesiones
    'django.contrib.messages',    # Sistema de mensajes
    'django.contrib.staticfiles',    # Archivos estáticos (CSS, JS, imágenes)
    'portafolio',     # Nuestra aplicación principal
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # sirve archivos estáticos en producción
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- URLS / TEMPLATES ---
ROOT_URLCONF = 'proyecto_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],    # Aquí se podrían agregar carpetas extras de plantillas
        'APP_DIRS': True,    # Busca plantillas dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',   # Permite usar request en templates
                'django.contrib.auth.context_processors.auth',   # Manejo de usuarios autenticados
                'django.contrib.messages.context_processors.messages',
                "portafolio.context_processors.theme_from_cookie",    # Nuestro procesador para tema claro/oscuro
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_django.wsgi.application'


# --- BASE DE DATOS ---
# Usa SQLite por defecto, pero Railway puede configurarla con dj_database_url
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"
    )
}

# --- VALIDACIÓN DE CONTRASEÑAS ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# --- INTERNACIONALIZACIÓN ---
LANGUAGE_CODE = 'en-us'     # Idioma por defecto

TIME_ZONE = 'UTC'   # Zona horaria

USE_I18N = True   # Traducciones

USE_TZ = True    # Manejo de zonas horarias


# --- ARCHIVOS ESTÁTICOS ---    
STATIC_URL = 'static/'    # URL base para servir estáticos
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")   # Carpeta usada en producción

# --- MODELO DE IDs ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 