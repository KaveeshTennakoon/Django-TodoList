from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('todo/', views.todolist, name='todo'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
    path('complete/<int:task_id>/', views.update_task_completion, name='update_task_completion'),
    path('logout/', views.user_logout, name='user_logout'),
    path('update/<int:id>', views.update_todo, name='update_todo')
]