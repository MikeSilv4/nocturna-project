from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

def catalog(request):
    context = {}
    return render(request, 'home/catalog/index.html', context)

def homepage(request):
    context = {}
    return render(request, 'home/homepage/index.html', context)

def contacts(request):
    context = {}
    return render(request, 'home/contacts/index.html', context)

def sucess(request):
    context = {}
    return render(request, 'home/sucess/index.html', context)
