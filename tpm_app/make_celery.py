from factory import create_app as app


ap = app()
ap.app_context().push()


# app context
# celery -A worker --loglevel=INFO.
# celery -A celery_worker.celery worker --loglevel=INFO.
