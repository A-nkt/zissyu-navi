"""
Django settings for zissyu_navi project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import environ

env = environ.Env()
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

env.read_env(os.path.join(BASE_DIR,'.env'))



# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'ud#90yv)ao6y2dn_4ps27gtdhq_%i4-016fyf7u-zku3nv6=e0'
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

#ALLOWED_HOSTS = ['hospeee.com','188.166.190.15']

# Application definition

INSTALLED_APPS = [
    'accounts',
    'ckeditor_uploader',
    'ckeditor',
    'main_app',
    'about_me',
    'media_service',
    'widget_tweaks',#フォームのcssを可変的にする
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

CKEDITOR_UPLOAD_PATH = 'uploads/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware', #login rate limit
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend', #login rate limit
    'django.contrib.auth.backends.ModelBackend',
]

SECURE_SSL_REDIRECT = False
ROOT_URLCONF = 'zissyu_navi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'zissyu_navi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'mysite',
#        'USER':'mysiteuser',
#        'PASSWORD':'mysiteuserp@S5',
#        'HOST':'localhost',
#        'PORT':'5432',
#        'ATOMIC_REQUESTS':True,
#    }
#}

DATABASE = {}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1
LOGOUT_REDIRECT_URL = 'main_app:home'


##################
### RECAPTCHA  ###
##################

GOOGLE_RECAPTCHA_SECRET_KEY = env('RECAPTCHA_SECRET_KEY')


#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#PROJECT_NAME = os.path.basename(BASE_DIR)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_URL = '/static/'
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)
#STATIC_ROOT = '/var/www/mysite'



CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_IMAGE_BACKEND = "pillow"

#MEDIA_URL = '/media/'
#MEDIA_ROOT = '/var/www/mysite/media'
