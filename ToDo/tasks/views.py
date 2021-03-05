from django.shortcuts import render, redirect
from .models import Tasks

def show_tasks(request):
    tasks = Tasks.objects.all()
    data = {'tasks':tasks}
    return render(request,'index.html',data)


#create the tasks
def create_task(request):
    task = request.POST.get('task')
    if request.POST:
        if task == "":
            return redirect('/')
        else:
            Tasks.objects.create(task=task)
    return redirect('/')
    
#show the task for edit
def edit_task(request):
    id_task = request.GET.get('id')
    dados = {}
    if id_task:
        dados['edit']= Tasks.objects.get(id=id_task)
        return render(request, 'index.html',dados)

#edit the task
def submit_edit(request):
    task = request.POST.get('task')
    id_task = request.POST.get('id_task')
    if id_task:
        if task == "":
            return redirect('/')
        else:
            Tasks.objects.filter(id=id_task).update(task=task)
            return redirect('/')


#delete tasks
def delete_task(request,id):
    Tasks.objects.get(id=id).delete()
    return redirect('/')