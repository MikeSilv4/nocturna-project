from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

def sale_item(request):
    context = {}
    return render(request, 'sales/sale_item/index.html', context)