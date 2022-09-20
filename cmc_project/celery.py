import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cmc_project.settings')

app = Celery('cmc_project')
app.config_from_object('django.conf:settings', namespace='CELERY')


# celery beat configuration.
# Key name is the function to execute periodically appended by the time between each execution
# Value is a dict with 2 keys:
# task: the path to the task to execute (here get_coins_data)
# schedule: the time between each executions.

app.conf.beat_schedule = {
    'get_coins_data_10s': {
        'task': 'coins.tasks.get_coins_data',
        'schedule': 10.0
    }
}

app.autodiscover_tasks()