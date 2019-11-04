from celery import shared_task

@shared_task
def push_date_to_parse(**data):
    print('Test')
