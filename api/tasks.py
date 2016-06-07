# from djcelery import celery

# @celery.task
# def add(x,y):
# 	return x + y

# @celery.task
# def sleeptask(i):
# 	from time import sleep
# 	sleep(i)
# 	return i

from celery import current_task, shared_task
from time import sleep

@shared_task()
def do_something(str):
	for i in range(100):
		sleep(0.1)
		current_task.update_state(state='PROGRESS',
			meta={'current': i, 'total': 100})