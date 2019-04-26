from rest_framework import serializers
from .models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    class Meta:
        model = TaskList
        fields = '__all__'
 
class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.CharField()
    due_on = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    task_list = TaskListSerializer()


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'status')


