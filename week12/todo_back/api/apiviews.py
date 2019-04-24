from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Task, TaskList
from .serializers import TaskListSerializer, TaskSerializer, TasksSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskListDetail(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Task.objects.filter(task_list_id=self.kwargs["task_list_id"])
        return queryset
    serializer_class = TaskSerializer

class TasksList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Task.objects.filter(id=1)
        return queryset
    serializer_class = TasksSerializer

class TaskDetail(generics.RetrieveDestroyAPIView):
    def get_queryset(self):
        queryset = Task.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class = TaskSerializer