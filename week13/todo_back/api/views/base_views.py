from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer
from django.http import HttpResponse


def index(request):
    context = {
        'name': 'User 1',
        'nums': [i for i in range(5)],
        'is_logged_in': False,
        'task': {
            'id': 1,
            'name': 'Task 1'
        },
        'tasks': [{
            'id': i,
            'name': 'Task {}'.format(i)
        } for i in range(5)]
    }
    return render(request, 'index.html', context)

def show_tasks(request, pk):
    return HttpResponse('<h1>{}</h1>'.format(pk))

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            # create function from serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=body)
        if serializer.is_valid():
            # update function from serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


def task_list_task(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.tasks.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)