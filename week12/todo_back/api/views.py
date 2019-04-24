from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, TaskList
from .serializers import TaskList, TaskListSerializer, TaskListSerializer2, TaskSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TaskLists(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListDetail(APIView):
    def get_object(request, task_list_id):
        try:
            queryset = Task.objects.filter(task_list_id=task_list_id)
            serializer = TaskSerializer(queryset, many=True)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, task_list_id, format=None):
        task_list = Task.objects.filter(task_list_id=task_list_id)
        serializer = TaskSerializer(task_list, many=True)
        return Response(serializer.data)

    def put(self, request, task_list_id, format=None):
        task_list = TaskList.objects.get(id=task_list_id)
        serializer = TaskListSerializer(task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_list_id, format=None):
        task_list = TaskList.objects.get(id=task_list_id)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskList1(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
                    raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)