from django.shortcuts import render
from django.http import HttpResponse

def sales(request):
    return render(request, 'sales/catalog/index.html')
