from factory import celery


@celery.task()
def add_two(x, y):
    print("cool:::")
    print(x+y)
    return x + y