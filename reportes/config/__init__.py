from __future__ import absolute_import, unicode_literals
from .settings.base import *
import os
from pathlib import Path


try:
    if bool(os.environ.get("DEBUG")) == True:
        from .settings.dev import *
        os.environ.setdefault("DJANGO_LOG_LEVEL","ERROR")
    else:
        from .settings.prod import *

    MIDDLEWARE.append("config.middleware.ErrorHandlerMiddleware.ErrorMiddleware")
    INSTALLED_APPS.append("corsheaders")
    INSTALLED_APPS.append("apps.auth_user")
    
except Exception as e:
    print(e)


from .celery import app as celery
__all__ = ('app',)