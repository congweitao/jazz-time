#!/usr/bin/python3

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','jazz_time.settings')

celery_app = Celery('jazz_time')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
