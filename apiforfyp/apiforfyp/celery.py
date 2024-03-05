from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#setting the Djanngo settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiforfyp.settings')
app = Celery('apiforfyp')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Look for task module in the project and load them

app.autodiscover_tasks()