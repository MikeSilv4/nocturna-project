import django
import os
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()                                                                                                                                              
from time import sleep

from src.apps.items.models import Items   
from src.apps.items.api.serializers import ItemsAllFieldsSerializer         

for i in range(1000):
    Items.objects.create(
        name=f"Vibrador {i}k",
        brand="test",
        model="test",
        description="test",
        category="vibradores",
        stock_quantity=10,
        value=1,
        image="https://avatars.githubusercontent.com/u/103974890?v=4"
    )