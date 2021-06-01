from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   # return HttpResponse("<h1 style='color:red'>home page of hello</h1>")
    return render(request,"hello/home.html")

def about(request):
    #return HttpResponse("<h1 style='color:blue'>About page of hello</h1>")
    return render(request,"hello/about.html")

def greetings(request,name):
    return render(request,"hello/greetings.html",{
        "username":name
    })
