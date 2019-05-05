from rest_framework import serializers
from .models import TaskList, Task
from django.contrib.auth.models import User


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        # {'name': 'new category 3'}
        # name='new category 3'
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)
 
class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'due_on' ,'task_list_id')

class TaskListSerializer3(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')

class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status')

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_by = UserSerializer(read_only=True)
    # tasks = TaskSerializer2(many=True)
    
    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by')

    def create(self, validated_data):
        # tasks = validated_data.pop('tasks')
        task_list = TaskList.objects.create(**validated_data)
        # for task in tasks:
        #     Task.objects.create(task_list=task_list, **task)
        return task_list