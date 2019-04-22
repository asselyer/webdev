from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, TaskList

def task_list(request):
    task_lists = TaskList.objects.all()
    json_task_lists = [l.to_json() for l in task_lists ]
    return JsonResponse(json_task_lists, safe=False)


def task_list_detail(request, task_list_id):
    tasks = Task.objects.filter(task_list_id=task_list_id)
    data = {"results": list(tasks.values(
        "id", 
        "name", 
        "status" ,"created_at", "task_list"))
        }
    return JsonResponse(data)


def task_list_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = task_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)
