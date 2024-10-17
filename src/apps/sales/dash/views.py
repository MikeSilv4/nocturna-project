from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

def catalog(request):
    context = {}
    return render(request, 'home/catalog/index.html', context)