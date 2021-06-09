from django.urls import  path
from .views import flight_home
urlpatterns=[
        path("home",flight_home,name="flight_home")
]