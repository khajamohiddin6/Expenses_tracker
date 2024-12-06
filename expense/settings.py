import os
import environ
from pathlib import Path

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Reads the .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key, Debug Mode, and Allowed Hosts from .env file
SECRET_KEY = env('SECRET_KEY', default='your_default_secret_key')  # Pull from .env, with default fallback
DEBUG = env.bool('DEBUG', default=False)  # Use False as default if DEBUG is not set
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])  # Defaults to localhost

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',  # Your app here
    'whitenoise.runserver_nostatic',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'expense.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Update if you have custom templates
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

WSGI_APPLICATION = 'expense.wsgi.application'

# Database configuration from .env file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME', default='expense_tracker_db'),
        'USER': env('DATABASE_USER', default='root'),
        'PASSWORD': env('DATABASE_PASSWORD', default='khajapspk123@A'),
        'HOST': env('DATABASE_HOST', default='localhost'),
        'PORT': env('DATABASE_PORT', default=3306),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'public/static']  # Ensure this folder exists
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Folder to collect static files

# Whitenoise static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'public/media'  # Folder for uploaded files

# Login Redirect URL
LOGIN_REDIRECT_URL = '/'

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
