from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages

from apps.first_app.models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request,'first_app/index.html', context)

def add(request):

    errors = Course.objects.basic_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            
        return redirect('/')

    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect('/')

def show(request, id):
    context = {
        'show': Course.objects.get(id=id)
    }
    return render(request,'first_app/show.html', context)

def delete(request, id):
    context = {
        'show': Course.objects.get(id=id)
    }
    this = Course.objects.get(id=id)
    this.delete()
    return redirect('/', context)