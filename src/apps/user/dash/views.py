from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from src.apps.user.models import CustomUser


def Login(request):
    context = {}
    return render(request, 'user/login/index.html', context)

def Create(request):
    context = {}
    return render(request, 'user/create/index.html', context)

def ForgotPassword(request):
    context = {}
    return render(request, 'user/forgot_password/index.html', context)

def Update(request):

    email = request.user.email
    
    if email:
        user = CustomUser.objects.filter(email=email).first()
    else:
        user = None

    context = {
        "user" : user
    }

    return render(request, 'user/update/index.html', context)