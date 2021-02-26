"""
WSGI config for zissyu_navi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zissyu_navi.settings') #本番環境
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zissyu_navi.local') #開発環境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zissyu_navi.settings.production")

application = get_wsgi_application()
