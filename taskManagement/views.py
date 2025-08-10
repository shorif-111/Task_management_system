from django.shortcuts import render,redirect
from TaskModel.models import Task
from TaskModel.forms import TaskForm
from TaskCategory.models import Category


def home(request):
    task = Task.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'home.html', {'task': task, 'categories': categories}) 


