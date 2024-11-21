from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

def sale_item(request):
    context = {}
    return render(request, 'sales/sale_item/index.html', context)

def bag(request):
    context = {}
    return render(request, 'sales/bag/index.html', context)

def favorite_item(request):
    context = {}
    return render(request, 'sales/favorite_item/index.html', context)

def view_item(request):
    context = {}
    return render(request, 'sales/view_item/index.html', context)

def promotions(request):
    context = {}
    return render(request, 'sales/promotions/index.html', context)