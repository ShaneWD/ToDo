from django.shortcuts import render
from .models import Task
# Create your views here.
def home(request):
    context = {
        "tasks":Task.objects.all()
    }
    

    return render(request, "main/home.html", context)