from django.urls import  path
from .views import flight_home,flight_detail,book
urlpatterns=[
        path("home",flight_home,name="flight_home"),
        path("detail/<int:flight_id>",flight_detail,name="flight-detail"),
        path("book/<int:flight_id>", book, name="flight-book"),

]