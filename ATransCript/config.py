class Config(object):
    BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    ALLOWED_EXTENTIONS = ['m4a', 'mp3', 'wav']
    UPLOAD_FOLDER = "controllers/uploads"