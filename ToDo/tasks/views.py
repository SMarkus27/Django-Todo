from django.shortcuts import render, redirect
from .models import Tasks

def show_tasks(request):
    tasks = Tasks.objects.all()
    data = {'tasks':tasks}
    return render(request,'index.html',data)

def create_tasks(request):
    task = request.POST.get('task')
    if request.POST:
        if task == "":
            return redirect('/')
        else:
            Tasks.objects.create(task=task)
    return redirect('/')