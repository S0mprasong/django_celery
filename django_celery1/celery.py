from __future__ import absolute_import
   
import os
from celery import Celery
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery1.settings')

from django.conf import settings   
app = Celery('django_celery1')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)