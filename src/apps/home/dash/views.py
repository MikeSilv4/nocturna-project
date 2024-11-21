from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from src.apps.user.models import CustomUser

def catalog(request):

    email = request.user.email
    
    if email:
        user = CustomUser.objects.filter(email=email).first()
    else:
        user = None

    context = {
        "user" : user
    }
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
