import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cats_gallery.settings')

app = Celery('cats_gallery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf['worker_prefetch_multiplier'] = 1

app.conf.beat_schedule = {
    'get_cat_url_10s': {
        'task': 'cats.tasks.get_cat_url',
        'schedule': 40.0,
    }
}

app.autodiscover_tasks()