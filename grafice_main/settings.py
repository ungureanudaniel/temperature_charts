from pathlib import Path
import os
from django.conf import settings
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.

load_dotenv(verbose=True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1', 'graficetemperatura.ro', 'www.graficetemperatura.ro']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'temperature_data',
    # 'axes',
    'captcha',
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
    # 'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'grafice_main.urls'
# AUTHENTICATION_BACKENDS = [
#     'axes.backends.AxesBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]
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

WSGI_APPLICATION = 'grafice_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if (os.environ.get('DJANGO_DEV') == 'True'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
# Production database
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }

INTERNAL_IPS = [
    "127.0.0.1",
]
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
WHITENOISE_AUTOREFRESH = True

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'ro'

TIME_ZONE = 'Europe/Bucharest'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AXES_ENABLED = os.environ.get("AXES_ENABLED")
# AXES_FAILURE_LIMIT = os.environ.get("AXES_FAILURE_LIMIT")
# AXES_COOLOFF_TIME = os.environ.get("AXES_COOLOFF_TIME")
# AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = os.environ.get("AXES_LOCK_OUT_BY")
# ATOMIC_REQUESTS = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
#-------------------EMAIL SETTINGS---------------------------------------------
FROM_EMAIL = 'contact@obcinastanisoarei.ro'
#------------------------MESSAGES SETTINGS--------------------------------------
try:
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
    }
except Exception as e:
    pass

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
CRISPY_TEMPLATE_PACK = 'uni_form'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DJANGO_DEV = True
