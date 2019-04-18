from django.db import models
from django.conf import settings
from django.utils import timezone

class TaskList(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(blank = True, null=True)
    status = models.CharField(max_length=50, null=True)
    task_list = models.ForeignKey(TaskList, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name