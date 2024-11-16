from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

def login(request):
    context = {}
    return render(request, 'user/login/index.html', context)

def create(request):
    context = {}
    return render(request, 'user/create/index.html', context)

def view(request):
    context = {}
    return render(request, 'user/view/index.html', context)