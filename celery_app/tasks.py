import time
import os

from celery_app import app

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
@app.task
def add(x, y):
    time.sleep(0.5)
    return x + y

