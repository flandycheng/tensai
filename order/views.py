# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404

# index page; home page
def index(request):
    return HttpResponse("Hey, welcome to %s index page " % (__file__))
