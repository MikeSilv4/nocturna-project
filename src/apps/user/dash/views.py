from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from src.apps.user.models import CustomUser

def login(request):
    context = {}
    return render(request, 'user/login/index.html', context)

def create(request):
    context = {}
    return render(request, 'user/create/index.html', context)

def view(request):
    
    user = CustomUser.objects.get(id=request.user.pk)
    user.born_date = user.born_date.strftime("%Y-%m-%d")
    context = {"user" : user}
    return render(request, 'user/view/index.html', context)