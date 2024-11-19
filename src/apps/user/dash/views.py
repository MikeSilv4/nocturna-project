from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

def Login(request):
    context = {}
    return render(request, 'user/login/index.html', context)

def ForgotPassword(request):
    context = {}
    return render(request, 'user/forgot_password/index.html', context)

def CreateAccount(request):
    context = {}
    return render(request, 'user/create_account/index.html', context)