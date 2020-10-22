from celery.schedules import timedelta
from celery.schedules import crontab


# Broker and Backend
# 指定 Broker
BROKER_URL = 'redis://127.0.0.1:6379'
# 指定 Backend
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_PREFETCH_MULTIPLIER = 10  # 并发量
CELERY_TASK_RESULT_EXPIRES = 3600 # 结果过期
CELERY_TASK_ALWAYS_EAGER = False # 如果是这样True，所有任务将通过阻塞在本地执行，直到任务返回
CELERY_ENABLE_UTC = False

# Timezone
CELERY_TIMEZONE="Asia/Shanghai"    # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'

# import 指定导入的任务模块
CELERY_IMPORTS = (
    'celery_app.tasks',
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_app.tasks.add',
         'schedule': crontab(minute="*"),       # 每 60 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
}