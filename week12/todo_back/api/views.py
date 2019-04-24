from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, TaskList
from .serializers import TaskList, TaskListSerializer, TaskListSerializer2, TaskSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def task_list_list(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
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
def task_list_detail(request, task_list_id):
    try:
        task_list = Task.objects.filter(task_list_id=task_list_id)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer2(task_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=body)
        if serializer.is_valid():
            # update function from serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})



def task_detail(request, pk):
    try:
        task = Task.objects.filter(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    if request.method == 'GET':
        serializer = TaskListSerializer2(task, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'error': 'bad request'})
