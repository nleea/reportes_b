from __future__ import absolute_import, unicode_literals
from .settings.base import *
import os
from pathlib import Path
from .celery import app as celery

try:
    if bool(os.environ.get("DEBUG")) == True:
        from .settings.dev import *
        os.environ.setdefault("DJANGO_LOG_LEVEL","ERROR")
    else:
        from .settings.prod import *

    INSTALLED_APPS.append("corsheaders")
    
except Exception as e:
    print(e)

__all__ = ('app',)