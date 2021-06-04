from django.shortcuts import render,redirect
from django import  forms

class NewTaskForm(forms.Form):
    task=forms.CharField(max_length=30)
    priority=forms.IntegerField(min_value=1,max_value=5)


tasks=['book appointment','check email','check balance','do recharge','book tickets']
# Create your views here.
def listtask(request):
    return render(request,"tasks/listtask.html",{
        "tasks_data":tasks
    })

def addtask(request):
    form=NewTaskForm()
    if request.method=='POST':
        print('inside post')
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks.append(request.POST['task'])
            print('redirect')
            return redirect('task-list')
        else:
            return render(request, "tasks/addtask.html", {
                "form": form
            })

    return render(request,"tasks/addtask.html",{
        "form":form
    })