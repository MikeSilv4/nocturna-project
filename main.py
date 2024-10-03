import django
import os
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()                                                                                                                                              
from time import sleep

from src.apps.items.models import Items   
from src.apps.items.api.serializers import ItemsAllFieldsSerializer         

for i in range(100):
    base = {"name" : f"name{i}", "brand" : f"brand{i}", "model" : f"model{i}", "description" : f"desc{i}"}

    serializer = ItemsAllFieldsSerializer(data=base)
    if serializer.is_valid():
        serializer.save()
    else:
        print("error")