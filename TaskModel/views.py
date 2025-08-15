from django.shortcuts import render, redirect
from .forms import TaskForm, UserRegistrationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
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
   
def profile(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('log_in')
    return render(request, 'TaskModel/profile.html', {'user': request.user})
def log_in(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'TaskModel/log_in.html', {'form': form})
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'TaskModel/register.html', {'form': form})
def logout(request):
    auth_logout(request)
    return redirect('log_in')