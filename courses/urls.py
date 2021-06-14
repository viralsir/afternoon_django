from django.urls import  path
from .views import *
urlpatterns=[
        path("new/",NewCourseView.as_view(),name="course-new"),
        path("view/",ListCourseView.as_view(),name="course-view"),
        path("update/<int:pk>",UpdateCourseView.as_view(),name="course-update"),
        path("delete/<int:pk>",DeleteCourseView.as_view(),name="course-delete")
]