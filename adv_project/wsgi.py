"""
WSGI config for adv_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

path = r'C:\Users\John\Desktop\Django_MUD\CS-Build-Week-1\adv_project'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adv_project.settings')

application = get_wsgi_application()
