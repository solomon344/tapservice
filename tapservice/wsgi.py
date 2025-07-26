"""
WSGI config for tapservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tapservice.settings')
from django.conf import settings

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
# application.add_files("/path/to/more/static/files", prefix="more-files/")