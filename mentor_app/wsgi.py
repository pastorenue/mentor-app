"""
WSGI config for mentor_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys 

from django.core.wsgi import get_wsgi_application
filedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(filedir)
sys.path.append(os.path.join(basedir, 'apps'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mentor_app.production_settings")


# application = get_wsgi_application()
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)