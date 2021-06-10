from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import flight,passenger

# Create your views here.
def flight_home(request):
    flights=flight.objects.all()
    return render(request,"airline/flight_home.html",{
        "flights":flights
    })

def flight_detail(request,flight_id):
    flight_info=flight.objects.get(id=flight_id)
    return render(request,"airline/flight_detail.html",{
        "flight":flight_info,
        "passengers":flight_info.passengers.all(),
        "non_passenger":passenger.objects.exclude(flights=flight_info).all()
    })

def book(request,flight_id):
    if request.method == 'POST':
        flight_info=flight.objects.get(id=flight_id)
        passenger_info=passenger.objects.get(id=request.POST['npassenger'])
        passenger_info.flights.add(flight_info)
        passenger_info.save()
        return redirect('flight_home')