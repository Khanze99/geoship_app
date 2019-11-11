from __future__ import absolute_import, unicode_literals
from celery.task import periodic_task
from celery import shared_task
from celery.schedules import crontab
from .upload_to_db import check_files


@periodic_task(run_every=crontab(minute=0, hour=0), name="push_date_to_parse")
def push_date_to_parse():
    check_files()
