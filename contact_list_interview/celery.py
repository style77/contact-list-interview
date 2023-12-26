import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contact_list_interview.settings")
app = Celery("contact_list_interview")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
