
from pathlib import Path
import os
import environ
from .base import *

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env.read_env(os.path.join(BASE_DIR,'.env'))

DEBUG = True

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']


############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/images/'
MEDIA_ROOT = BASE_DIR


####################
## Email Settings ##
####################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
