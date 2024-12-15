from pathlib import Path
import os

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-$edcsaoscyk!_=ii0n*%#te!4t8(=dfw89s1wgo-cc!3f9=#iy'
DEBUG = True
ALLOWED_HOSTS = []

# Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'chat',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configuration
ROOT_URLCONF = 'RentCar.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# WSGI
WSGI_APPLICATION = 'RentCar.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_bd',
        'USER': 'najm',
        'PASSWORD': 'najm',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'voiture_bd': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'car_bd',
        'USER': 'najm',
        'PASSWORD': 'najm',
        'HOST': 'localhost',
        'PORT': '5432',
    },
        'reservation_bd': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'reservation_bd',
        'USER': 'najm',
        'PASSWORD': 'najm',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# Authentication
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
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/'
LOGOUT_REDIRECT_URL = '/users/login/'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'users/static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default Primary Key Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
