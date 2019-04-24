from django.urls import path
from .views import TaskLists, TaskListDetail, TaskDetail, TaskList1

urlpatterns =[
path("task_list/", TaskLists.as_view(), name="task_list"),
#path("task_list/", task_list_list),
path("task_list/<int:task_list_id>/", TaskListDetail.as_view(), name="task_list_detail"),
#path("task_list/<int:task_list_id>/", task_list_detail, name="task_list_detail"),
path("task_list/<int:task_list_id>/tasks/", TaskLists, name="tasks_list"),
#path("tasks/<int:pk>/", TaskDetail.as_view(), name="task_detail")
path("tasks/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
path("tasks/", TaskList1.as_view())
]
