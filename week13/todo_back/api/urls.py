from django.urls import path
from api import views

urlpatterns = [
    path('task_list/', views.TaskLists.as_view()),
    path('task_list/<int:pk>/', views.TaskListDetail.as_view()),
    path('task_list/<int:pk>/tasks/', views.TaskListTask.as_view()),
    # path('task_list/', views.task_lists),
    # path('task_list/<int:pk>/', views.task_list_detail),
    # path('task_list/<int:pk>/tasks/', views.task_list_task),

    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),

    path('', views.index),
    #path('tasks/<int:pk>/', views.show_tasks),

]