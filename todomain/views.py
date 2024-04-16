from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')# - is giving to show in desc order
    ctasks = Task.objects.filter(is_completed=True)
    data={
        'tasks':tasks,
        'ctasks':ctasks,
    }
    return render(request,'home.html',data)