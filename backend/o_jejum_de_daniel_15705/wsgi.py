"""
WSGI config for o_jejum_de_daniel_15705 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'o_jejum_de_daniel_15705.settings')

application = get_wsgi_application()
