# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404

from project.models import Project

# index page; home page
def index(request):
    return render(request, 'project/index.html', {})

def list(request):
    project_list = Project.objects.all()
    return render(request, 'project/list.html', {
        'project_list':project_list
    })
