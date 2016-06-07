# Create your views here.
from django.http import HttpResponse, JsonResponse
from api import tasks
from celery.result import AsyncResult
import simplejson as json

def test_celery(request):
	# result = tasks.sleeptask.delay(10)
	# result_one = tasks.sleeptask.delay(10)
	# result_two = tasks.sleeptask.delay(10)
	result = tasks.do_something.delay('Celery Test')
	html = "<a target='_blank' href='/check_task_status/"+result.task_id+"'>"+result.task_id+"</a>"
	return HttpResponse(html)

def check_task_progress(request,task_id):
	task = AsyncResult(task_id)
	data = task.result or task.state
	return HttpResponse(json.dumps(data))