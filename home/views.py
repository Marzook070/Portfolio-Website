from django.http import HttpResponse
from django.shortcuts import render
from .models import Projects

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def projects(request):
    projects_data = Projects.objects.all()
        
    return render(request, 'pages/projects.html', {'projects': projects_data})