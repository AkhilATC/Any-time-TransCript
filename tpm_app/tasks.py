import factory

CELERY_APP = factory.celery()


@CELERY_APP.task(name="add_up", bind=True)
def console_tasks(param, param2):
    print("control here")
    print(param+param2)
    return param + param2

