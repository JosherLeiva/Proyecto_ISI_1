"""
WSGI config for ProyectoDistribuidora_J_J_J project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDistribuidora_J_J_J.settings')

application = get_wsgi_application()
