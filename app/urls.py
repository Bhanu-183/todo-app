from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.login,name="logincheck"),
    path("tasks",views.tasks,name="tasks"),
    path("register",views.register,name="register"),
    path("remove/<int:task_id>",views.remove,name="remove"),
    path("completed/<int:task_id>",views.completed,name="completed"),
]