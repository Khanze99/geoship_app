from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoship_app.settings')

app = Celery('geoship_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {}".format(self.request))

#
# app.conf.beat_schedule = {
#     'upload_to_db': {
#         'task': 'geoship_app.geoships_info_app.tasks.push_date_to_parse',
#         'schedule': crontab()
#     }
# }