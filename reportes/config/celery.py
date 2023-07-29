from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")

app = Celery("reportes")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.enable_utc = False

app.conf.update(timezone="America/Bogota")
app.conf.update(broker_url="redis://127.0.0.1:6379")
app.conf.update(accept_content=['application/json'])
app.conf.update(task_serializer="json")
app.conf.update(result_serializer="json")
app.autodiscover_tasks()
