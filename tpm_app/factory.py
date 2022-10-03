from flask import Flask
from controllers.speech_processor_module import speech_processor
from celery import Celery


celery = Celery(__name__, include=["controllers.tasks"])


def create_app():
    application = Flask(__name__)
    application.config.from_object('config.Config')
    application.register_blueprint(speech_processor)
    print(application.config)
    celery.conf.update(application.config)
    # celery.init_app(app)
    return application

def create_celery_app():
    application = Flask(__name__)
    application.config.from_object('config.Config')
    application.register_blueprint(speech_processor)
    print(application.config)
    celery.conf.update(application.config)
    # celery.init_app(app)
    return application
def return_celery_app():
    return celery

