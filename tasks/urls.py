from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.taskList, name='task-list'),
]
