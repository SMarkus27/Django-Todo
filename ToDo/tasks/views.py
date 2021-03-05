from django.shortcuts import render
from .models import Tasks

def show_tasks(request):
    tasks = Tasks.objects.all()
    data = {'tasks':tasks}
    return render(request,'index.html',data)

    