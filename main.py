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
        image="https://http2.mlstatic.com/vibrador-hitachi-magic-wand-extreme-2-accesorios-punto-g-cli-D_NQ_NP_886377-MLM41070968113_032020-F.jpg"
    )