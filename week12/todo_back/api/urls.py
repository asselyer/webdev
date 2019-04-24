# from django.urls import include, path
# from rest_framework import routers
# from api.views import TaskView, TaskListView

# router = routers.DefaultRouter()
# router.register('task', TaskView)
# router.register('task_list', TaskListView)

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ] 
from django.urls import path
from .apiviews import TaskList, TaskListDetail, TasksList, TaskDetail
from .views import task_list_list, task_list_detail, task_detail

urlpatterns = [
#path("task_list/", TaskList.as_view(), name="task_list"),
path("task_list/", task_list_list),
#path("task_list/<int:task_list_id>/", TaskListDetail.as_view(), name="task_list_detail"),
path("task_list/<int:task_list_id>/", task_list_detail, name="task_list_detail"),
path("task_list/<int:task_list_id>/tasks/", task_list_list, name="tasks_list"),
#path("tasks/<int:pk>/", TaskDetail.as_view(), name="task_detail")
path("tasks/<int:pk>/", task_detail, name="task_detail")

]
