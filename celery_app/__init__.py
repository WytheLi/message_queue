from celery import Celery


app = Celery('celeryApp')
app.config_from_object('celery_app.celeryconfig')