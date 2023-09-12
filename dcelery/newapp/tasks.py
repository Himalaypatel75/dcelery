from celery import shared_task
import time

@shared_task(task_rate_limit='10/m', queue='celery') #per task wise limit
def tp1(a, b, message = None):
    result = a+b
    if message:
        result = f"{message} : {result}"
    time.sleep(3)
    return result

@shared_task(queue='celery:1')
def tp2():
    time.sleep(3)
    return

@shared_task(queue='celery:2')
def tp3():
    time.sleep(3)
    return

@shared_task(queue='celery:3')
def tp4():
    time.sleep(3)
    return