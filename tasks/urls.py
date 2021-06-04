from django.urls import path
from .views import listtask,addtask
urlpatterns=[
        path("list/",listtask,name="task-list"),
        path("new/",addtask,name="task-add")
]