from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, TaskList

def task_list(request):
    MAX_OBJECTS = 20
    task_list = TaskList.objects.all()[:MAX_OBJECTS]
    data = {"results": list(task_list.values("id", "name" ))}
    return JsonResponse(data)

# def task_list_detail(request, pk):
#     MAX_OBJECTS = 20
#     task_lists = Task.objects.all(pk=id)[:MAX_OBJECTS]
#     data = {"results": list(tasks.values("id", "name", "status" ,"created_at"))}
#     return JsonResponse(data)

def task_list_detail(request, task_list_id):
    tasks = Task.objects.filter(task_list_id=task_list_id)
    data = {"results": list(tasks.values(
        "id", 
        "name", 
        "status" ,"created_at", "task_list"))
        }
    return JsonResponse(data)

