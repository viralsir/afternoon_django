from django.shortcuts import render
from .models import flight

# Create your views here.
def flight_home(request):
    flights=flight.objects.all()
    return render(request,"airline/flight_home.html",{
        "flights":flights
    })