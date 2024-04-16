from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def addTask(request):
    taskp=request.POST['task']
    Task.objects.create(task=taskp) #in task model there are 4 fields task,is completed,creted and updated,task field is mandotory and is completed is default is false so we dn have to give here,created and updated automatically add
    # return HttpResponse('sub')
    return redirect('home') # home is a fn in views.py in todomain

def markAsDone(request,id):
    task=get_object_or_404(Task,id=id)
    task.is_completed=True
    task.save()
    return redirect('home')

def markAsunDone(request,id):
    task=get_object_or_404(Task,id=id)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit(request,id):
    gettask=get_object_or_404(Task,id=id)
    if request.method=='POST':
        new_task=request.POST['task']
        gettask.task = new_task
        gettask.save()
        return redirect('home')
    else:
        gettasks={
            'tasks': gettask,
        }
        return render(request,'edit.html',gettasks)

def delete(request,id):
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect('home')