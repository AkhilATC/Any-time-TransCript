import os


class Config(object):

    BROKER_URL = "redis://172.20.0.2:6379/1"
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND", "redis://172.20.0.2:6379/0"
    )