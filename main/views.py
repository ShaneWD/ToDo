from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    context = {
        "tasks":Task.objects.all(),
        "form": form
    }
    

    return render(request, "main/home.html", context)

def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    context = {'form': form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (request, "main/update.html", context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {
        "item": item,
        "tasks":Task.objects.all(),
    }
    return render(request, 'main/delete.html', context)