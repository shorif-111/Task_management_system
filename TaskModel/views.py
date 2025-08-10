from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'TaskModel/add_task.html', {'form': form})
def task_edit(request, id):
    task_edit = Task.objects.get(pk=id)
    form = TaskForm(instance=task_edit)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task_edit)
    return render(request, 'TaskModel/add_task.html', {'form': form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')

def complete_task(request, id):
    task = Task.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')
   