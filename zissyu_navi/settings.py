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
from .base import *

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent


env.read_env(os.path.join(BASE_DIR,'.env'))

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'ud#90yv)ao6y2dn_4ps27gtdhq_%i4-016fyf7u-zku3nv6=e0'
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['hospeee.com','188.166.190.15']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite',
        'USER':'mysiteuser',
        'PASSWORD':'mysiteuserp@S5',
        'HOST':'localhost',
        'PORT':'5432',
        'ATOMIC_REQUESTS':True,
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
            )
STATIC_ROOT = '/var/www/mysite'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/mysite/media'
# mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
