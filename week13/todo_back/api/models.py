from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    
    objects = TaskListManager()

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(blank = True, null=True)
    status = models.CharField(max_length=50, null=True)
    task_list = models.ForeignKey(TaskList, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'due_on': self.due_on,
            'status': self.status,
        }

