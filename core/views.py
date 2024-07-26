from django.shortcuts import render
from .models import Project


def homeview(request):
    return render(request, 'core/base.html')


def project_listview(request):
    data = Project.objects.all()
    return render(request, 'core/projects.html', data)