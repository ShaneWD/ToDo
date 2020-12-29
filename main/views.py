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