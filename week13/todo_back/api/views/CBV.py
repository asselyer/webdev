from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer, TaskSerializer2
from rest_framework.permissions import IsAuthenticated


class TaskLists(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListDetail(APIView):
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer2(task_list)
        return Response(serializer.data)

    def put(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer2(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_list = self.get_object(pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListTask(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        task = Task.objects.filter(task_list_id=pk)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

